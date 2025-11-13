from rest_framework.serializers import ModelSerializer

from children.models import Children, Application


class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = Children
        fields = "__all__"


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
