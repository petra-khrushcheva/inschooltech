from datetime import datetime
from time import sleep

import pytest
from indicators.models import (Indicator, IndicatorsMetric, Metric, Reference,
                               Score)
from public.models import Lab, Test


@pytest.fixture(autouse=True)
def lab():
    lab_1 = Lab.objects.create(
        name='Lab 1',
        id='5032d958-93ff-4e64-b620-6507753100ac'
    )
    return lab_1


# Фикстура для модели Test
@pytest.fixture(autouse=True)
def assessment(lab):
    time_1 = datetime.now()
    sleep(5)
    time_2 = datetime.now()
    labtest = Test.objects.create(
        id='217f0c27-36bb-4336-946b-64a1dfd1bc27',
        started_at=time_1,
        completed_at=time_2,
        lab_id=lab
    )
    return labtest


@pytest.fixture(autouse=True)
def indicator():
    ind_1 = Indicator.objects.create(
        name='способность к усвоению информации',
        id='cccdada8-de75-4974-ab58-e0233722b956'
    )
    return ind_1


@pytest.fixture(autouse=True)
def metric():
    metric_1 = Metric.objects.create(
        name='Скорость реакции',
        unit='Секунды',
        id='815dee15-338c-4470-bdfa-53ad069bba73'
    )
    return metric_1


@pytest.fixture(autouse=True)
def ind_metric(indicator, metric):
    ind_metric_1 = IndicatorsMetric.objects.create(
        indicator_id=indicator,
        metric_id=metric,
        id='74a0ec4a-12ed-4641-b506-50638f0ea650'
    )
    return ind_metric_1


@pytest.fixture(autouse=True)
def reference(ind_metric):
    ref_1 = Reference.objects.create(
        min_score=0,
        max_score=10,
        indicator_metric_id=ind_metric,
        id='7e6f82cf-09d7-492e-84a0-464016604a02'
    )
    return ref_1


@pytest.fixture(autouse=True)
def score(assessment, ind_metric):
    score_1 = Score.objects.create(
        score=3,
        test_id=assessment,
        indicator_metric_id=ind_metric,
        id='24363974-49ed-405a-a200-d98fd08c6a9f'
    )
    return score_1
