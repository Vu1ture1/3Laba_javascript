# Generated by Django 4.2.13 on 2024-05-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_promocode_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pick_up_point',
            field=models.CharField(default='', max_length=100),
        ),
    ]
