# Generated by Django 4.2.13 on 2024-05-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0035_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='phone_number',
            field=models.CharField(default=None, max_length=13),
        ),
    ]
