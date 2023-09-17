from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Test
from .serializers import TestSerializer


class TestAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('lab_id', 'is_active')
