#
# 자유게시판 1에 대한 모델
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/09/05 21:30 created.
#


from django.db import models


class BBSFree1(models.Model):
    _AUTHOR_MAX_LENGTH = 16
    _TITLE_MAX_LENGTH = 128
    _MAIN_TEXT_LENGTH = 65536

    # 게시글 본연의 ID
    id = models.BigAutoField(primary_key=True)

    # 게시글 메타데이터 (조회수, 추천수, 삭제여부)
    views = models.BigIntegerField(
        default=0,
        null=False,
        blank=False,
    )
    recommended_count = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    is_deleted = models.BooleanField(
        default=False,
    )

    # 작성자 정보 컬럼
    author = models.CharField(
        max_length=_AUTHOR_MAX_LENGTH,
        null=False,
        blank=False,
    )
    author_ip = models.GenericIPAddressField(
        null=False,
        blank=False,
    )

    # 본문 정보 컬럼
    title = models.CharField(
        max_length=_TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )
    main_text = models.CharField(
        max_length=_MAIN_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    # 게시글에 대한 MAC time
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
