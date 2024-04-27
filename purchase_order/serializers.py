from rest_framework import serializers
from purchase_order import models

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = "__all__"