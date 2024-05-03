from .models import PurchaseOrder
from django.db.models import Avg, ExpressionWrapper, F, fields, Sum

def calculate_average_response_time(vendor):
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = acknowledged_pos.annotate(
        response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())
    )
    total_response_time = response_times.aggregate(total_response_time=Sum('response_time'))['total_response_time']
    total_acknowledged_pos = acknowledged_pos.count()

    if total_acknowledged_pos > 0:
        average_response_time_seconds = total_response_time.total_seconds() / total_acknowledged_pos
        average_response_time_minutes = average_response_time_seconds / 60
    else:
        average_response_time_minutes = None

    return average_response_time_minutes


def calculate_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='Completed')
    on_time_pos = completed_pos.filter(delivered_date__lte=F('delivery_date'))
    total_completed_pos = completed_pos.count()

    if total_completed_pos > 0:
        on_time_delivery_rate = on_time_pos.count() / total_completed_pos * 100
    else:
        on_time_delivery_rate = 0.0

    return on_time_delivery_rate

def calculate_quality_rating_average(vendor):
    completed_pos_with_rating = PurchaseOrder.objects.filter(vendor=vendor, status='Completed').exclude(quality_rating=None)
    total_completed_pos = completed_pos_with_rating.count()

    if total_completed_pos > 0:
        quality_rating_average = completed_pos_with_rating.aggregate(avg_quality_rating=Avg('quality_rating'))
    else:
        quality_rating_average = None

    return quality_rating_average["avg_quality_rating"]


def calculate_fulfillment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    completed_pos = total_pos.filter(status='Completed')
    fulfilled_pos = completed_pos.exclude(issues__isnull=False)

    total_pos_count = total_pos.count()
    fulfilled_pos_count = fulfilled_pos.count()

    if total_pos_count > 0:
        fulfillment_rate = fulfilled_pos_count / total_pos_count * 100
    else:
        fulfillment_rate = 0.0

    return fulfillment_rate
