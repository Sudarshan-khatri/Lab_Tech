# Generated by Django 5.2 on 2025-05-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('team', '0003_rename_team_name_team_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Team_member',
            field=models.ManyToManyField(related_name='member', to='accounts.account'),
        ),
    ]
