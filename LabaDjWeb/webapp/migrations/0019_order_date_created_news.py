# Generated by Django 4.2.13 on 2024-05-21 14:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_alter_basketitem_medicine_alter_medicine_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 5, 21, 14, 7, 34, 737551, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_message', models.CharField(default=None, max_length=300)),
                ('med', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.medicine')),
            ],
        ),
    ]
