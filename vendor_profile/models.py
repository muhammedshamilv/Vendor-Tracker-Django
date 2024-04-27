from django.db import models
from VendorTreacker.models import AbstractBaseModel

class Vendor(AbstractBaseModel):
    name = models.CharField(max_length=150)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=150)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)
    
class HistoricalPerformance(AbstractBaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()