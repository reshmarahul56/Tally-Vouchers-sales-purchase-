# Generated by Django 4.0.6 on 2022-10-12 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0059_alter_stock_item_allocat_godown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creategodown',
            name='comp',
        ),
    ]
