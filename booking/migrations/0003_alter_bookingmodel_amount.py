# Generated by Django 5.2 on 2025-05-09 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_bookingmodel_created_at_bookingmodel_updated_at'),
        ('servicemanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='Amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount', to='servicemanagement.servicemanagement'),
        ),
    ]
