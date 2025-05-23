# Generated by Django 5.2 on 2025-05-07 07:31

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(blank=True, max_length=300, null=True)),
                ('Email', models.EmailField(blank=True, max_length=300, null=True)),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('Role', models.CharField(choices=[('Technician', 'Technician'), ('Supervisor', 'Supervisor'), ('Assistant', 'Assistant'), ('Manager', 'Manager'), ('Admin', 'Admin')], max_length=300, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('joined_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
