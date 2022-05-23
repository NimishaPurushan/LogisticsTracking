from django.shortcuts import render
from rest_framework import  viewsets, generics, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import get_current_timezone
import pytz
# Create your views here.
from .models import * 
from .serializer import *


class ItemList(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


class ShipmentList(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def create(self, request):
        print(request.data)
        item_id = request.data["item_id"]
        quantity = int(request.data["quantity"])
        shipment_data=ShipmentSerializer(data=request.data)
        if shipment_data.is_valid():
            shipment_data.save()
        order_list = Shipment.objects.values_list('order_id', flat=True)
        order_id = order_list[len(order_list)-1]
        tracking_id = Shipment.objects.get(order_id=order_id).tracking_id
        _shipment = Shipment.objects.get(order_id=order_id)
        try:
            if request.data["fast_delivery"]:
                _shipment.expected_delivery = timezone.now() + timedelta(hours=24)
                _shipment.shipping_charge = 10
            else:
                _shipment.expected_delivery = timezone.now() + timedelta(hours=240)
                _shipment.shipping_charge = 0
        except KeyError:
            _shipment.expected_delivery = timezone.now() + timedelta(hours=240)
            _shipment.shipping_charge = 0
        _shipment.save()
        item = Items.objects.get(item_id=item_id)
        if item.quantity < quantity:
            return Response("Out of stock", status=status.HTTP_400_BAD_REQUEST)
        else:
            item.quantity = item.quantity-quantity  # change field
            item.save()
            return Response({"Order Id": order_id,
                            "Tracking Id": tracking_id,
                            "expected_delivery":_shipment.expected_delivery,
                            "shipping_charge": _shipment.shipping_charge,
                            "Total Cost(including shipping charge)": (quantity*int(item.item_price))
                                                                        + _shipment.shipping_charge
            }, status=status.HTTP_200_OK)