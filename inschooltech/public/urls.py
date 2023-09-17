from django.urls import path

from .views import TestAPIView

urlpatterns = [
    path('tests/', TestAPIView.as_view(), name='test-list'),
]
