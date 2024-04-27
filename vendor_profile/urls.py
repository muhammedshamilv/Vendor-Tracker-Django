from django.urls import path
from vendor_profile import views

urlpatterns = [
    path("", views.VendorListCreateAPIView.as_view(), name="Vendor_create_list"),
    path("<uuid:id>/", views.VendorDetailsAPI.as_view(), name="vendor-details"),
]