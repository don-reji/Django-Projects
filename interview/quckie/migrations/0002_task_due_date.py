# Generated by Django 4.2.5 on 2023-12-18 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quckie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 19, 7, 38, 23, 307804, tzinfo=datetime.timezone.utc)),
        ),
    ]