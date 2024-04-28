from rest_framework import generics,status
from purchase_order import serializers
from purchase_order import models
import uuid
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating purchase orders.

    Allows users to list all purchase orders with an option to filter by vendor,
    or create a new purchase order.

    - GET: Returns a list of all purchase orders with an option to filter by vendor.
    - POST: Creates a new purchase order.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PurchaseOrderSerializer

    def get_queryset(self):
        queryset = models.PurchaseOrder.objects.all()
        vendor_id = self.request.query_params.get('vendor_id')
        if vendor_id:
            try:
                uuid.UUID(vendor_id) 
            except ValueError:
                raise ParseError("Invalid vendor_id")

            queryset = queryset.filter(vendor=vendor_id)
        return queryset

class PurchaseOrderDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a purchase order.

    Allows users to retrieve details of a specific purchase order, update an existing
    purchase order, or delete a purchase order.

    - GET: Returns details of a specific purchase order.
    - PUT: Updates an existing purchase order.
    - DELETE: Deletes a purchase order.
    """
    permission_classes = [IsAuthenticated]
    queryset = models.PurchaseOrder.objects.all()
    serializer_class = serializers.PurchaseOrderSerializer
    lookup_field = 'id'
    
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except models.PurchaseOrder.DoesNotExist:
            return Response({"message": "Purchase order not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Purchase order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)