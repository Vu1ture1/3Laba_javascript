# Generated by Django 4.2.13 on 2024-05-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='basket',
            field=models.ManyToManyField(default=None, related_name='medicines', to='webapp.medicine'),
        ),
    ]
