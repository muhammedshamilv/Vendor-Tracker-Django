from django.urls import path
from purchase_order import views

urlpatterns = [
    path("", views.PurchaseOrderListCreateAPIView.as_view(), name="purchase_order_list_create"),
    path("<uuid:id>/", views.PurchaseOrderDetailsAPIView.as_view(), name="purchase_order_detail"),
    path('<uuid:id>/acknowledge/', views.AcknowledgePurchaseOrderAPIView.as_view(), name='acknowledge_purchase_order'),
    
]