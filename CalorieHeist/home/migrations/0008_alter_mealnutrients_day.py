# Generated by Django 3.2.8 on 2021-10-12 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_mealnutrients_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealnutrients',
            name='day',
            field=models.DateField(default=datetime.date.today),
        ),
    ]