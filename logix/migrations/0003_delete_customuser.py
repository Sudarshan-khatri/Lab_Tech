# Generated by Django 5.1.5 on 2025-05-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logix', '0002_remove_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
