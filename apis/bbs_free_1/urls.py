#
# 자유게시판 1의 URL 경로
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2021/09/12 16:35 created.
#


from django.urls import path

from apis.bbs_free_1 import views

app_name = "bbs_free_1"
urlpatterns = [
    path("", view=views.BBSFree1List.as_view(), name="list"),
    path("write", view=views.BBSFree1Create.as_view(), name="create"),
    path("<int:post_id>", view=views.BBSFree1Retrieve.as_view(), name="retrieve"),
]
