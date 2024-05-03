from django.db import models
from VendorTreacker.models import AbstractBaseModel
from vendor_profile.models import Vendor
from datetime import timedelta
from django.utils import timezone

class PurchaseOrder(AbstractBaseModel):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    status_choices = ((PENDING,PENDING),(COMPLETED,COMPLETED),(CANCELED,CANCELED))
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(default=timezone.now() + timedelta(days=2))
    delivered_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100,choices = status_choices, default=PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now())
    issues = models.TextField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
