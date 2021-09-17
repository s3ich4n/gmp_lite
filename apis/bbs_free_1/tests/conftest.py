import pytest


@pytest.fixture(scope="module")
def new_post():
    """ """
    new_post = {
        "author": "ㅇㅇ",
        "title": "제목",
        "main_text": "본문",
    }

    yield new_post
