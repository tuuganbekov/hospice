from django.urls import path

from children.views import (
    ChildrenListAPIView,
    ApplicationCreateAPIView,
    ChildRetrieveAPIView
)

urlpatterns = [
    path("children/", ChildrenListAPIView.as_view()),
    path("children/<int:pk>/", ChildRetrieveAPIView.as_view()),
    path("application/", ApplicationCreateAPIView.as_view()),
]
