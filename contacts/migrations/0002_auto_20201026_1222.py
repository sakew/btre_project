# Generated by Django 3.1 on 2020-10-26 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contacts_date',
            new_name='contact_date',
        ),
    ]
