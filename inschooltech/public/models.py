from config.basemodels import BaseModel
from django.db import models


class Lab(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(BaseModel):
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    lab_id = models.ForeignKey(
        Lab,
        on_delete=models.PROTECT,
        related_name="tests")

    def __str__(self):
        return f'{self.id}'
