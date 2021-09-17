from rest_framework import generics, permissions

from apis.bbs_free_1.api import serializers
from apis.bbs_free_1.models import BBSFree1


class BBSFree1Create(generics.CreateAPIView):
    """게시글을 생성한다"""

    queryset = BBSFree1.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.BBSFree1CreateSerializer


class BBSFree1List(generics.ListAPIView):
    """삭제되지 않은 게시글 전체를 조회한다"""

    queryset = BBSFree1.objects.filter(is_deleted=False).all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.BBSFree1ListSerializer


class BBSFree1Retrieve(generics.RetrieveAPIView):
    """게시글을 조회한다"""

    lookup_field = "id"
    lookup_url_kwarg = "post_id"

    queryset = BBSFree1.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.BBSFree1RetrieveSerializer
