from rest_framework import serializers

from children.models import Children, Application


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def validate(self, attrs):
        app_type = attrs.get("type") or getattr(self.instance, "type", None)
        child = attrs.get("child") if "child" in attrs else getattr(self.instance, "child", None)

        if app_type != Application.Type.DREAM and child is None:
            raise serializers.ValidationError(
                {"child": "This field is required for this type of application."}
            )

        return attrs
