# Generated by Django 4.2.13 on 2024-05-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_alter_medicine_all_sold_num_alter_review_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
