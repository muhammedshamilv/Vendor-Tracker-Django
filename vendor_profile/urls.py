from django.urls import path
from vendor_profile import views

urlpatterns = [
    path("", views.Vendors.as_view(), name="Vendor_list"),
]