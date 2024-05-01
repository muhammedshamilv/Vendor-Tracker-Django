from rest_framework.response import Response
from rest_framework import status, generics
from vendor_profile import serializers
from vendor_profile import models
from rest_framework.permissions import IsAuthenticated
class VendorListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating vendors.

    Allows users to list all existing vendors or create a new vendor.

    - GET: Returns a list of all vendors.
    - POST: Creates a new vendor.
    Permissions:
    - IsAuthenticated: Users must be authenticated to access this endpoint.
    """
    permission_classes = [IsAuthenticated]
    
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

class VendorDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving , updating and deleting vendors.

    Allows users to retrieve vendor details or update existing vendor or delete a vendor.

    - GET: Returns details of a vendors.
    - PUT: Updates existing vendor.
    - DELETE: Delete existing vendor.
    
    Permissions:
    - IsAuthenticated: Users must be authenticated to access this endpoint.
    
    """
    permission_classes = [IsAuthenticated]
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    lookup_field = 'id'
    
    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except models.Vendor.DoesNotExist:
            return Response({"message": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Vendor deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class VendorPerformanceAPIView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving performance metrics of a specific vendor.

    Retrieves the calculated performance metrics for a specific vendor.

    Parameters:
    - id (UUID): The unique identifier of the vendor.

    Returns:
    - HTTP 200 OK: Returns the performance metrics data for the specified vendor.

    Permissions:
    - IsAuthenticated: Users must be authenticated to access this endpoint.
    """

    permission_classes = [IsAuthenticated]
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_data, status=status.HTTP_200_OK)
    