# Generated by Django 5.1.5 on 2025-06-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('role', models.CharField(blank=True, max_length=400, null=True)),
                ('lab', models.ManyToManyField(related_name='member', to='lab.labmodel')),
            ],
        ),
    ]
