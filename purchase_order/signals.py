from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import calculate_average_response_time
from django.db.models.signals import post_save
from django.utils import timezone
from django.db.models import Q
from vendor_profile.models import HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if not created and instance.acknowledgment_date is not None:
        print("instance", instance)
        vendor = instance.vendor
        average_response_time = calculate_average_response_time(vendor)
        
        current_date = timezone.now().date()
        try:
            historical_performance = HistoricalPerformance.objects.get(
                vendor=vendor,
                created_at__date=current_date
            )
            historical_performance.average_response_time = average_response_time
            historical_performance.save()
        except HistoricalPerformance.DoesNotExist:
            historical_performance = HistoricalPerformance.objects.create(
                vendor=vendor,
                average_response_time=average_response_time,
                on_time_delivery_rate=0.0,
                quality_rating_avg=0.0,
                fulfillment_rate=0.0
            )

        vendor.average_response_time = average_response_time
        vendor.save()
        
        
# Todo // write signals for other fields updated in purchase order  and use the util functions to update HistoricalPerformance and Vendor