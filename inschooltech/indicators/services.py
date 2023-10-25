from .models import Reference


def within_normal_range(obj):
    reference = Reference.objects.get(
          indicator_metric_id=obj.indicator_metric_id)
    if reference.min_score <= obj.score <= reference.max_score:
        return True
    return False
