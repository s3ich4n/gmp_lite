import pytest
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from apis.bbs_free_1.views import BBSFree1Create

pytestmark = pytest.mark.django_db


class TestCreateBBSCh1NormalUser:
    """자유게시판 1의 게시글 생성과 관련한 테스트

    정상유저: 도배를 안함
    """

    def test_create_post_should_return_201_when_normal_user_try_to_post(
        self,
        new_post,
    ):
        """ """
        factory = APIRequestFactory()

        view = BBSFree1Create.as_view()

        request = factory.post(
            reverse("bbs_free_1:list_create"),
            data=new_post,
        )

        response = view(request)

        assert response.status_code == 201


class TestCreateBBsCh1AbnormalUser:
    def test_create_post_should_return_400_when_banned_user_try_to_post(
        self,
        new_post,
    ):
        """비정상 유저가 글을 쓰면 등록되지 말아야 한다(400)."""
        factory = APIRequestFactory()
        view = BBSFree1Create.as_view()

        request = factory.post(
            reverse("bbs_free_1:list_create"),
            data=new_post,
            REMOTE_ADDR="1.2.3.4",
        )

        response = view(request)

        assert response.status_code == 400
