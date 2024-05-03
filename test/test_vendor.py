from unittest.mock import Mock, patch
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from vendor_profile.models import Vendor
from django.contrib.auth import get_user_model

class VendorListCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_list_create_url = reverse('Vendor_create_list')
        self.mock_vendor_data = [
            {'id': 1, 'name': 'Vendor 1', 'address': 'Address 1'},
            {'id': 2, 'name': 'Vendor 2', 'address': 'Address 2'}
        ]
        
            
    def create_test_user(self):
        User = get_user_model()
        return User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')


    @patch('vendor_profile.views.VendorListCreateAPIView.get_queryset')
    def test_get_vendors_unauthorized(self, mock_get_queryset):
        mock_get_queryset.return_value = Vendor.objects.none()
        response = self.client.get(self.vendor_list_create_url)
        print("test_get_vendors_unauthorized", response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @patch('vendor_profile.views.VendorListCreateAPIView.get_queryset')
    @patch('vendor_profile.views.VendorListCreateAPIView.get_serializer')
    def test_get_vendors_authorized(self, mock_get_serializer, mock_get_queryset):
        mock_get_queryset.return_value = Vendor.objects.none()
        mock_serializer = Mock(data=self.mock_vendor_data)
        mock_get_serializer.return_value = mock_serializer
        user = self.create_test_user()
        self.client.force_authenticate(user=user)
        response = self.client.get(self.vendor_list_create_url)
        print("test_get_vendors_authorized", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('vendor_profile.views.VendorListCreateAPIView.create')
    def test_create_vendor_unauthorized(self, mock_create):
        mock_create.side_effect = Exception('Unauthorized')
        data = {'name': 'New Vendor', 'address': 'New Address'}
        response = self.client.post(self.vendor_list_create_url, data, format='json')
        print("test_create_vendor_unauthorized", response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)