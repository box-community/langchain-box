import pytest
from langchain_community.document_loaders.blob_loaders.schema import Blob
from pytest_mock import MockerFixture

from langchain_box.blob_loaders import BoxBlobLoader
from langchain_box.utilities import BoxAuth, BoxAuthType


# Test auth types
def test_direct_token_initialization() -> None:
    loader = BoxBlobLoader(  # type: ignore[call-arg]
        box_developer_token="box_developer_token",
        box_file_ids=["box_file_ids"],
    )

    assert loader.box_developer_token == "box_developer_token"
    assert loader.box_file_ids == ["box_file_ids"]


def test_failed_direct_token_initialization() -> None:
    with pytest.raises(ValueError):
        loader = BoxBlobLoader(box_file_ids=["box_file_ids"])  # type: ignore[call-arg] # noqa: F841


def test_auth_initialization() -> None:
    auth = BoxAuth(
        auth_type=BoxAuthType.TOKEN, box_developer_token="box_developer_token"
    )

    loader = BoxBlobLoader(  # type: ignore[call-arg]
        box_auth=auth,
        box_file_ids=["box_file_ids"],
    )

    assert loader.box_file_ids == ["box_file_ids"]


# test loaders
def test_failed_file_initialization() -> None:
    with pytest.raises(ValueError):
        loader = BoxBlobLoader(box_developer_token="box_developer_token")  # type: ignore[call-arg] # noqa: F841


def test_folder_initialization() -> None:
    loader = BoxBlobLoader(  # type: ignore[call-arg]
        box_developer_token="box_developer_token",
        box_folder_id="box_folder_id",
    )

    assert loader.box_developer_token == "box_developer_token"
    assert loader.box_folder_id == "box_folder_id"


# test Document retrieval
def test_file_load(mocker: MockerFixture) -> None:
    mocker.patch(
        "langchain_box.utilities._BoxAPIWrapper.get_blob_from_file_id",
        return_value=[],
    )

    loader = BoxBlobLoader(  # type: ignore[call-arg]
        box_developer_token="box_developer_token",
        box_file_ids=["box_file_ids"],
    )

    documents = loader.yield_blobs()
    assert documents

    mocker.patch(
        "langchain_box.utilities._BoxAPIWrapper.get_blob_from_file_id",
        return_value=(
            Blob(
                id="id",
                metadata={"source": "source", "name": "name", "file_size": 1},
                data="data\n",
                mimetype="text/plain",
                encoding="utf-8",
                path="https://app.box.com",
            )
        ),
    )

    loader = BoxBlobLoader(  # type: ignore[call-arg]
        box_developer_token="box_developer_token",
        box_file_ids=["box_file_ids"],
    )

    for blob in loader.yield_blobs():
        assert isinstance(blob, Blob)
        assert blob.id == "id"
        assert blob.metadata["source"] == "source"
        assert blob.metadata["name"] == "name"
        assert blob.metadata["file_size"] == 1
        assert blob.data == "data\n"
        assert blob.mimetype == "text/plain"
        assert blob.encoding == "utf-8"
        assert blob.path == "https://app.box.com"
