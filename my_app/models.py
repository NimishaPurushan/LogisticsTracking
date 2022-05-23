from datetime import datetime
from django.db import models
import string
import random
from django.utils import timezone
from django.utils.timezone import make_aware
import pytz


# Create your models here.
class Items(models.Model):
    item_id  = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.item_name


def generate_tracking_id():
    characters = string.ascii_letters + string.digits 
    tracking_id = ''.join(random.choice(characters) for i in range(8))
    return tracking_id


class Shipment(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.CharField(max_length=50)
    shipment_address = models.CharField(max_length=500)
    order_date = models.DateTimeField(default=timezone.now, editable=False)
    expected_delivery = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    delicate_item = models.BooleanField()
    fast_delivery = models.BooleanField()
    shipping_charge = models.IntegerField(blank=True,
                                          editable=False,
                                          default=0)
    tracking_id = models.CharField(max_length = 10,
        blank=True,
        editable=False,
        default=generate_tracking_id)


