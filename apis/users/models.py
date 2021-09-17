from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for GMP."""

    name = models.CharField(
        _("Name of User"),
        null=False,
        blank=False,
        max_length=32,
    )
    # 계정정보에 닉네임을 어떻게 가져갈 수 있는지 알아봐야함
    # nickname = models.CharField(
    #     _("Alias of User"),
    #     unique=True,
    #     max_length=32,
    # )

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    # 유저 메타데이터
    banned_until = models.DateTimeField(null=True)

    REQUIRED_FIELDS = [
        "nickname",
    ]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
