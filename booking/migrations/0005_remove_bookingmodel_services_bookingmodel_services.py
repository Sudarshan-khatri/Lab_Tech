# Generated by Django 5.2 on 2025-05-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_bookingmodel_amount'),
        ('servicemanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='Services',
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='Services',
            field=models.ManyToManyField(blank=True, related_name='servicemgt', to='servicemanagement.servicemanagement'),
        ),
    ]
