from django.contrib import admin
from vendor_profile import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.HistoricalPerformance)
