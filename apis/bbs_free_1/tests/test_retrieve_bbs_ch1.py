import pytest
from django.test import RequestFactory
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestRetrieveBBSCh1NormalUser:
    def test_retrieve_posts_should_return_200(
        self,
        rf: RequestFactory,
    ):
        """누구든지 게시판을 조회하면 볼 수 있어야 한다

        이 기능만큼은 어떻게든 죽지 않아야한다..

        """
        new_post = {}

        response = rf.get(
            reverse("bbs_list_create:create"),
            data=new_post,
        )

        assert response.status_code == 201
