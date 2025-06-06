# Generated by Django 5.2 on 2025-05-07 07:31

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Complete Blood Count (CBC)', 'Complete Blood Count'), ('Basic Metabolic Panel (BMP)', 'Basic Metabolic Panel'), ('Comprehensive Metabolic Panel (CMP)', 'Comphrensive Metabolic Panel'), ('Lipid Panel Cardiology', 'Lipid Panel Cardiology'), ('Liver Function Test (LFT)', 'Liver function test'), ('Thyroid Function Test (TFT)', 'Thyroid Function Test'), ('Urinalysisb urine', 'Urinalysisb urine'), ('HbA1c (Glycated Hemoglobin)', 'Hblc'), ('Cgulation Profile (PT, aPTT, INR)', 'Cgulation Profile'), ('vitamin Test', 'vitamin test')], max_length=200)),
                ('category', models.CharField(blank=True, choices=[('Biochemistry / Metabolic', 'Biochemistry / Metabolic'), ('Cardiology / Metabolic', 'Cardiology / Metabolic'), ('Hepatic / Biochemistry', 'Hepatic / Biochemistry'), ('Endocrinology', 'Endocrinology'), ('Nephrology', 'Nephrology'), ('Diabetes', 'Diabetes'), ('Hematology / Coagulation', 'Hematology / Coagulation'), ('Nutritional / Endocrinology', 'Nutritional / Endocrinology')], max_length=200)),
                ('price', models.DecimalField(choices=[(Decimal('40.00'), '$40'), (Decimal('30.00'), '$30'), (Decimal('50.00'), '$50'), (Decimal('60.00'), '$60'), (Decimal('40.00'), '$40'), (Decimal('30.00'), '$30'), (Decimal('50.00'), '$50'), (Decimal('60.00'), '$60')], decimal_places=2, default=0.0, max_digits=10)),
                ('Description', models.TextField(blank=True, max_length=5000)),
            ],
        ),
    ]
