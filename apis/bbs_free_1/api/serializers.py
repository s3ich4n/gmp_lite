from ipware import get_client_ip
from rest_framework import serializers

from apis.bbs_free_1.models import BBSFree1


class BBSFree1CreateSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs["author_ip"], _ = get_client_ip(self.context["request"])

        return attrs

    class Meta:
        model = BBSFree1
        fields = (
            "author",
            "title",
            "main_text",
        )


class BBSFree1ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBSFree1
        fields = (
            "id",
            "title",
            "author_ip",
        )


class BBSFree1RetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBSFree1
        fields = (
            "title",
            "main_text",
            "author",
            "author_ip",
        )
