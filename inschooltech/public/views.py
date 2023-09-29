from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.db.models import Prefetch

from indicators.models import Score
from .models import Test
from .serializers import TestSerializer


class TestAPIView(generics.ListAPIView):
    queryset = Test.objects.prefetch_related(
        Prefetch('results',
                 queryset=Score.objects.select_related(
                     'indicator_metric_id__metric_id',
                     'indicator_metric_id__indicator_id',
                     ).all()
                 ))
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('lab_id', 'is_active')

    @method_decorator(cache_page(60 * 10))
    def dispatch(self, *args, **kwargs):
        return super(TestAPIView, self).dispatch(*args, **kwargs)
