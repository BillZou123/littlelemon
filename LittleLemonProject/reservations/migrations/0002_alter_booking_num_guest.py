# Generated by Django 4.2.10 on 2024-05-20 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='num_guest',
            field=models.IntegerField(),
        ),
    ]
