# Generated by Django 4.2.13 on 2024-05-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0034_alter_vacancy_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(default=None, max_length=13),
        ),
    ]
