import ast
import os

import pytest
from langchain_community.document_loaders.blob_loaders.schema import Blob

from langchain_box.blob_loaders import BoxBlobLoader
from langchain_box.utilities import (
    BoxAuth,
    BoxAuthType,
    BoxMetadataQuery,
    BoxSearchOptions,
)
from langchain_box.utilities.box import SearchTypeFilter


@pytest.fixture()
def auth():  # type: ignore[no-untyped-def]
    BOX_USER_ID = "19498290761"

    box_client_id = os.getenv("BOX_CLIENT_ID")
    box_client_secret = os.getenv("BOX_CLIENT_SECRET")

    auth = BoxAuth(
        auth_type=BoxAuthType.CCG,
        box_client_id=box_client_id,
        box_client_secret=box_client_secret,
        box_user_id=BOX_USER_ID,
    )

    yield auth


@pytest.fixture()
def env_vars():  # type: ignore[no-untyped-def]
    BOX_FOLDER_ID = "275206526155"
    BOX_FIRST_FILE = "1724737576425"
    BOX_SECOND_FILE = "1724741335031"
    BOX_THIRD_FILE = "1724742143566"
    BOX_ENTERPRISE_ID = "899905961"
    BOX_METADATA_QUERY = "total >= :value"
    BOX_METADATA_PARAMS = '{ "value": 2 }'
    BOX_METADATA_TEMPLATE = "langchainintegrationtest"

    env_vars = {
        "box_folder_id": BOX_FOLDER_ID,
        "box_first_file": BOX_FIRST_FILE,
        "box_second_file": BOX_SECOND_FILE,
        "box_third_file": BOX_THIRD_FILE,
        "box_enterprise_id": BOX_ENTERPRISE_ID,
        "box_metadata_query": BOX_METADATA_QUERY,
        "box_metadata_params": BOX_METADATA_PARAMS,
        "box_metadata_template": BOX_METADATA_TEMPLATE,
    }

    yield env_vars


def test_one_file(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxBlobLoader(box_auth=auth, box_file_ids=[env_vars["box_first_file"]])

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()


def test_multiple_files(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxBlobLoader(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"], env_vars["box_second_file"]],
    )

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()


def test_folder(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxBlobLoader(box_auth=auth, box_folder_id=env_vars["box_folder_id"])

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()


def test_folder_recursive(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxBlobLoader(
        box_auth=auth, box_folder_id=env_vars["box_folder_id"], recursive=True
    )

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()


def test_search(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    box_search_options = BoxSearchOptions(
        ancestor_folder_ids=[env_vars["box_folder_id"]],
        search_type_filter=[SearchTypeFilter.NAME],
    )

    loader = BoxBlobLoader(
        box_auth=auth, query="test_file_3.docx", box_search_options=box_search_options
    )

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()


def test_metadata_query(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    params = ast.literal_eval(env_vars["box_metadata_params"])

    query = BoxMetadataQuery(
        template_key=f"enterprise_{env_vars['box_enterprise_id']}.{env_vars['box_metadata_template']}",
        query=env_vars["box_metadata_query"],
        query_params=params,
        ancestor_folder_id=env_vars["box_folder_id"],
    )

    loader = BoxBlobLoader(box_auth=auth, box_metadata_query=query)

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert (
            blob.id == env_vars["box_second_file"]
            or blob.id == env_vars["box_third_file"]
        )


def test_extra_fields(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    extra_fields = ["shared_link"]

    loader = BoxBlobLoader(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"]],
        extra_fields=extra_fields,
    )

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id in env_vars.values()
        assert "shared_link" in blob.metadata.keys()  # type: ignore
