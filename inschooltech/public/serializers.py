from drf_spectacular.utils import extend_schema_field
from indicators.serializers import ScoreSerializer
from rest_framework import serializers

from .models import Test


class TestSerializer(serializers.ModelSerializer):
    duration_seconds = serializers.SerializerMethodField()
    results = ScoreSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = ('id', 'lab_id', 'duration_seconds', 'results')

    @extend_schema_field(serializers.IntegerField)
    def get_duration_seconds(self, obj) -> int:
        return int((obj.completed_at - obj.started_at).total_seconds())
