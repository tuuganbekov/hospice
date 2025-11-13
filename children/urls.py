from django.urls import path

from children.views import ChildrenListAPIView, ApplicationCreateAPIView

urlpatterns = [
    path("children/", ChildrenListAPIView.as_view()),
    path("application/", ApplicationCreateAPIView.as_view()),
]