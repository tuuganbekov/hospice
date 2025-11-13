from rest_framework.generics import ListAPIView, CreateAPIView

from children.models import Children, Application
from children.serializers import ChildrenSerializer, ApplicationSerializer


class ChildrenListAPIView(ListAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    
    
class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
