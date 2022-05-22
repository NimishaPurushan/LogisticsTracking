# Generated by Django 3.2.13 on 2022-05-22 15:57

from django.db import migrations, models
import my_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_shipment_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='tracking_id',
            field=models.CharField(blank=True, default=my_app.models.generate_tracking_id, editable=False, max_length=10),
        ),
    ]
