from rest_framework.response import Response
from rest_framework import status, generics
from vendor_profile import serializers
from vendor_profile import models

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

class VendorDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
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