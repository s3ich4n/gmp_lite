import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_bbs_free_1_create():
    """ """
    assert reverse("bbs_free_1:create") == "/bbs1/write"
    assert resolve("/bbs1/write").view_name == "bbs_free_1:create"


def test_bbs_free_1_retrieve():
    """ """
    assert reverse("bbs_free_1:retrieve", kwargs={"post_id": 1}) == "/bbs1/1"
    assert resolve("/bbs1/1").view_name == "bbs_free_1:retrieve"


def test_bbs_free_1_list():
    """ """
    assert reverse("bbs_free_1:list") == "/bbs1/"
    assert resolve("/bbs1/").view_name == "bbs_free_1:list"
