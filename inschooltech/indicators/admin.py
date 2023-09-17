from config.basemodels import BaseAdminModel
from django.contrib import admin

from .models import Indicator, IndicatorsMetric, Metric, Reference, Score


class IndicatorAdmin(BaseAdminModel):
    list_display = ('id', 'name', 'description')


class IndicatorsMetricAdmin(BaseAdminModel):
    list_display = ('id', 'indicator_id', 'metric_id')


class MetricAdmin(BaseAdminModel):
    list_display = ('id', 'name', 'unit', 'description')


class ReferenceAdmin(BaseAdminModel):
    list_display = ('indicator_metric_id', 'min_score', 'max_score')


class ScoreAdmin(BaseAdminModel):
    list_display = ('id', 'score', 'test_id', 'indicator_metric_id')


admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(IndicatorsMetric, IndicatorsMetricAdmin)
admin.site.register(Metric, MetricAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Score, ScoreAdmin)
