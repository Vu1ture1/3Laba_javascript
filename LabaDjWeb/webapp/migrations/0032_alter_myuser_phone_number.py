# Generated by Django 4.2.13 on 2024-05-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0031_employee_f_name_employee_l_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(default=None, max_length=13),
        ),
    ]
