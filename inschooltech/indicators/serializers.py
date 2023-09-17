from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Reference, Score


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
                  'is_within_normal_range'
                  )

    @extend_schema_field(serializers.BooleanField)
    def get_is_within_normal_range(self, obj) -> bool:
        reference = Reference.objects.get(
            indicator_metric_id=obj.indicator_metric_id
        )
        if reference.min_score <= obj.score <= reference.max_score:
            return True
        return False
