from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Score
from .services import within_normal_range


class ScoreSerializer(serializers.ModelSerializer):
    indicator_name = serializers.CharField(
        source='indicator_metric_id.indicator_id.name'
    )
    metric_name = serializers.CharField(
        source='indicator_metric_id.metric_id.name'
    )
    metric_unit = serializers.CharField(
        source='indicator_metric_id.metric_id.unit'
    )
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ('id',
                  'score',
                  'indicator_name',
                  'metric_name',
                  'metric_unit',
                  'is_within_normal_range')

    @extend_schema_field(serializers.BooleanField)
    def get_is_within_normal_range(self, obj) -> bool:
        return within_normal_range(obj)
