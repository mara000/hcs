# Generated by Django 4.1.6 on 2023-02-12 14:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hcs_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Participant",
        ),
    ]
