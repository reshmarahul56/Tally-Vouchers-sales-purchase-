# Generated by Django 4.0.6 on 2022-10-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0053_rename_total_stock_item_allocation_total_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher_purchase',
            name='party_AC_name',
            field=models.CharField(default=True, max_length=225),
        ),
    ]
