# Generated by Django 5.1.3 on 2025-02-12 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_complaintregister_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaintregister',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
