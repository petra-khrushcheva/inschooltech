from config.basemodels import BaseModel
from django.db import models
from public.models import Test


class Indicator(BaseModel):
    name = models.CharField(max_length=200, verbose_name='indicator_name')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Metric(BaseModel):
    name = models.CharField(
        max_length=200,
        verbose_name='metric_name'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='metric_description'
    )
    unit = models.CharField(
        max_length=200,
        verbose_name='metric_unit'
    )

    def __str__(self):
        return self.name


class IndicatorsMetric(BaseModel):
    indicator_id = models.ForeignKey(Indicator, on_delete=models.PROTECT)
    metric_id = models.ForeignKey(Metric, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.indicator_id} - {self.metric_id}'


class Reference(BaseModel):
    min_score = models.DecimalField(max_digits=10, decimal_places=5)
    max_score = models.DecimalField(max_digits=10, decimal_places=5)
    indicator_metric_id = models.ForeignKey(
        IndicatorsMetric,
        on_delete=models.PROTECT
    )


class Score(BaseModel):
    score = models.DecimalField(max_digits=10, decimal_places=5)
    test_id = models.ForeignKey(
        Test,
        on_delete=models.PROTECT,
        related_name='results'
    )
    indicator_metric_id = models.ForeignKey(
        IndicatorsMetric,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return (f'{self.indicator_metric_id.indicator_id} - '
                '{self.indicator_metric_id.metric_id}'
                )
