from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from children.models import Children, Application
from children.pagination import CustomPagination
from children.serializers import (
    ChildrenSerializer,
    ApplicationSerializer
)


class ChildrenListAPIView(ListAPIView):
    queryset = Children.objects.filter(active=True)
    serializer_class = ChildrenSerializer
    pagination_class = CustomPagination


class ChildRetrieveAPIView(RetrieveAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

    
class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save()
        if data["type"] != "DREAM":
            child = data["child"]
            child.active = False
            child.save()
