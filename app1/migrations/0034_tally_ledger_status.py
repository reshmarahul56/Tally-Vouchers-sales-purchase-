# Generated by Django 4.0.4 on 2022-09-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_tally_group_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tally_ledger',
            name='status',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
