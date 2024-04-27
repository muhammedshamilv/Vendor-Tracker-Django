from django.db import models
from VendorTreacker.models import AbstractBaseModel
from vendor_profile.models import Vendor

class PurchaseOrder(AbstractBaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
