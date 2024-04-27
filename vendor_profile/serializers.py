from rest_framework import serializers
from vendor_profile import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = "__all__"