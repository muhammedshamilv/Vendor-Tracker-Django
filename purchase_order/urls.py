from django.urls import path
from purchase_order import views

urlpatterns = [
    path("", views.PurchaseOrders.as_view(), name="purchase_orders"),
]