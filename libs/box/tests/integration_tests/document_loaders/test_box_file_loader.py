import os

import pytest
from langchain_core.documents import Document

from langchain_box.document_loaders import BoxLoader
from langchain_box.utilities import BoxAuth, BoxAuthType


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

    env_vars = {
        "box_folder_id": BOX_FOLDER_ID,
        "box_first_file": BOX_FIRST_FILE,
        "box_second_file": BOX_SECOND_FILE,
    }

    yield env_vars


def test_one_file(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxLoader(box_auth=auth, box_file_ids=[env_vars["box_first_file"]])

    docs = loader.load()

    assert docs == [
        Document(
            page_content="Langchain integration test 1\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724737576425/versions/1899382753871/representations/extracted_text/content/",
                "title": "test_file_1_docx",
            },
        )
    ]


def test_multiple_files(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxLoader(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"], env_vars["box_second_file"]],
    )

    docs = loader.load()

    assert docs == [
        Document(
            page_content="Langchain integration test 1\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724737576425/versions/1899382753871/representations/extracted_text/content/",
                "title": "test_file_1_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 2\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724741335031/versions/1899370540709/representations/extracted_text/content/",
                "title": "test_file_2_docx",
            },
        ),
    ]


def test_folder(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxLoader(box_auth=auth, box_folder_id=env_vars["box_folder_id"])

    docs = loader.load()

    assert docs == [
        Document(
            page_content="Langchain integration test 1\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724737576425/versions/1899382753871/representations/extracted_text/content/",
                "title": "test_file_1_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 2\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724741335031/versions/1899370540709/representations/extracted_text/content/",
                "title": "test_file_2_docx",
            },
        ),
    ]


def test_folder_recursive(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    loader = BoxLoader(
        box_auth=auth, box_folder_id=env_vars["box_folder_id"], recursive=True
    )

    docs = loader.load()

    assert docs == [
        Document(
            page_content="Langchain integration test 3\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724742143566/versions/1899362450170/representations/extracted_text/content/",
                "title": "test_file_3_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 1\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724737576425/versions/1899382753871/representations/extracted_text/content/",
                "title": "test_file_1_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 2\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724741335031/versions/1899370540709/representations/extracted_text/content/",
                "title": "test_file_2_docx",
            },
        ),
    ]


def test_extra_fields(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    extra_fields = ["shared_link"]

    loader = BoxLoader(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"]],
        extra_fields=extra_fields,
    )

    for document in loader.lazy_load():
        assert isinstance(document, Document)
        assert "shared_link" in document.metadata.keys()  # type: ignore
