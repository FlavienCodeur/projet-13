# Generated by Django 3.0 on 2023-01-17 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_auto_20230117_0837'),
        ('profiles', '0002_auto_20230117_0842'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
