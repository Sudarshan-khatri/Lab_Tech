# Generated by Django 5.2 on 2025-05-09 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_rename_full_name_team_team_name_team_lab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Team_name',
            new_name='TeamName',
        ),
    ]
