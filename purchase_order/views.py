from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class PurchaseOrders(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"PO": "ok"})
