import os

import pytest
from langchain_core.documents import Document

from langchain_box.retrievers import BoxRetriever
from langchain_box.utilities import (
    BoxAuth,
    BoxAuthType,
    BoxSearchOptions,
    SearchTypeFilter,
)


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


def test_search(auth, env_vars):  # type: ignore[no-untyped-def]
    box_search_options = BoxSearchOptions(
        ancestor_folder_ids=[env_vars["box_folder_id"]],
        search_type_filter=[SearchTypeFilter.NAME],
    )

    retriever = BoxRetriever(box_auth=auth, box_search_options=box_search_options)

    docs = retriever.invoke("test_file_3.docx")

    assert docs == [
        Document(
            page_content="Langchain integration test 3\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724742143566/versions/1899362450170/representations/extracted_text/content/",
                "title": "test_file_3_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 2\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724741335031/versions/1899370540709/representations/extracted_text/content/",
                "title": "test_file_2_docx",
            },
        ),
        Document(
            page_content="Langchain integration test 1\n",
            metadata={
                "source": "https://dl.boxcloud.com/api/2.0/internal_files/1724737576425/versions/1899382753871/representations/extracted_text/content/",
                "title": "test_file_1_docx",
            },
        ),
    ]


def test_box_ai(auth, env_vars):  # type: ignore[no-untyped-def]
    retriever = BoxRetriever(box_auth=auth, box_file_ids=[env_vars["box_first_file"]])

    docs = retriever.invoke("summarize this file")

    assert docs is not None
    for doc in docs:
        assert doc.metadata == {
            "source": "Box AI",
            "title": "Box AI summarize this file",
        }


def test_box_ai_multiple(auth, env_vars):  # type: ignore[no-untyped-def]
    retriever = BoxRetriever(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"], env_vars["box_second_file"]],
    )

    docs = retriever.invoke("summarize this file")

    assert docs is not None
    for doc in docs:
        assert doc.metadata == {
            "source": "Box AI",
            "title": "Box AI summarize this file",
        }


def test_box_ai_citations(auth, env_vars):  # type: ignore[no-untyped-def]
    retriever = BoxRetriever(
        box_auth=auth, box_file_ids=[env_vars["box_first_file"]], citations=True
    )

    docs = retriever.invoke("summarize this file")

    assert docs is not None
    for doc in docs:
        assert (
            doc.metadata["source"] == "Box AI"
            or doc.metadata["source"] == "Box AI summarize this file"
        )


def test_box_ai_citations_only(auth, env_vars):  # type: ignore[no-untyped-def]
    retriever = BoxRetriever(
        box_auth=auth,
        box_file_ids=[env_vars["box_first_file"]],
        citations=True,
        answer=False,
    )

    docs = retriever.invoke("summarize this file")

    assert docs is not None
    for doc in docs:
        assert doc.metadata["source"] == "Box AI summarize this file"


def test_extra_fields(auth, env_vars) -> None:  # type: ignore[no-untyped-def]
    extra_fields = ["shared_link"]

    box_search_options = BoxSearchOptions(
        ancestor_folder_ids=[env_vars["box_folder_id"]],
        search_type_filter=[SearchTypeFilter.NAME],
    )

    retriever = BoxRetriever(  # type: ignore[call-arg]
        box_auth=auth, box_search_options=box_search_options, extra_fields=extra_fields
    )

    docs = retriever.invoke("test_file_3.docx")

    for document in docs:
        assert isinstance(document, Document)
        assert "shared_link" in document.metadata.keys()  # type: ignore
