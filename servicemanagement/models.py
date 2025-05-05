from django.db import models
from decimal  import Decimal

# Create your models here.
class ServiceManagement(models.Model):
    name_choice=[
        ('Complete Blood Count (CBC)','Complete Blood Count'),
        ('Basic Metabolic Panel (BMP)','Basic Metabolic Panel'),
	    ('Comprehensive Metabolic Panel (CMP)','Comphrensive Metabolic Panel'),	
        ('Lipid Panel Cardiology','Lipid Panel Cardiology'),
        ('Liver Function Test (LFT)','Liver function test'),
	    ('Thyroid Function Test (TFT)','Thyroid Function Test'),	
        ('Urinalysisb urine','Urinalysisb urine'), 
        ('HbA1c (Glycated Hemoglobin)','Hblc'),	
        ('Cgulation Profile (PT, aPTT, INR)','Cgulation Profile'),
        ('vitamin Test','vitamin test')
    ]
    category_choice=[
        ('Biochemistry / Metabolic','Biochemistry / Metabolic'),
	    ('Cardiology / Metabolic','Cardiology / Metabolic'),
	    ('Hepatic / Biochemistry','Hepatic / Biochemistry'),
        ('Endocrinology','Endocrinology'),
        ('Nephrology','Nephrology'),
        ('Diabetes','Diabetes'),
        ('Hematology / Coagulation','Hematology / Coagulation'),
        ('Nutritional / Endocrinology','Nutritional / Endocrinology')
        ]
    price_choice = [
        (Decimal('40.00'), '$40'),
        (Decimal('30.00'), '$30'),
        (Decimal('50.00'), '$50'),
        (Decimal('60.00'), '$60'),
        (Decimal('40.00'), '$40'),
        (Decimal('30.00'), '$30'),
        (Decimal('50.00'), '$50'),
        (Decimal('60.00'), '$60'),
]
    name=models.CharField(max_length=200,choices=name_choice,blank=True)
    category=models.CharField(max_length=200,choices=category_choice,blank=True)
    price=models.DecimalField(max_digits=10,choices=price_choice,decimal_places=2,default=0.00)
    Description=models.TextField(max_length=5000,blank=True)


    def __str__(self):
        return self.name