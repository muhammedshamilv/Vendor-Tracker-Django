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