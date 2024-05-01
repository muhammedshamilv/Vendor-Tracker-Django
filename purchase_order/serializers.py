from rest_framework import serializers
from purchase_order import models
from django.utils import timezone

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = "__all__"
        
    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        if status == 'Completed' and not instance.delivered_date:
            instance.delivered_date = timezone.now()
        return super().update(instance, validated_data)