# Generated by Django 4.2.13 on 2024-09-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0043_alter_aboutcompany_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcompany',
            name='legal_address',
        ),
    ]
