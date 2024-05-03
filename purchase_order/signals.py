from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import calculate_average_response_time,calculate_on_time_delivery_rate,calculate_fulfillment_rate,calculate_quality_rating_average
from django.db.models.signals import post_save
from django.utils import timezone
from django.db.models import Q
from vendor_profile.models import HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if not created and instance.acknowledgment_date is not None:
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
            )

        vendor.average_response_time = average_response_time
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, created, **kwargs):
    if not created and instance.status == "Completed":
        vendor = instance.vendor
        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        fulfillment_rate = calculate_fulfillment_rate(vendor)
        
        if instance.quality_rating is not None:
            quality_rating = calculate_quality_rating_average(vendor)
            
        current_date = timezone.now().date()
        try:
            historical_performance = HistoricalPerformance.objects.get(
                vendor=vendor,
                created_at__date=current_date
            )
            historical_performance.on_time_delivery_rate = on_time_delivery_rate
            historical_performance.fulfillment_rate = fulfillment_rate
            if quality_rating:
                historical_performance.quality_rating_avg = quality_rating
            historical_performance.save()
        except HistoricalPerformance.DoesNotExist:
            historical_performance = HistoricalPerformance.objects.create(
                vendor=vendor,
                on_time_delivery_rate=on_time_delivery_rate,
                fulfillment_rate = fulfillment_rate,
                quality_rating_avg = quality_rating if quality_rating else None    
            )
            
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.fulfillment_rate=fulfillment_rate
        if quality_rating:
            vendor.quality_rating_avg = quality_rating
        vendor.save()
        
