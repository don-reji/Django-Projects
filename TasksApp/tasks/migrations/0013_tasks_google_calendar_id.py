# Generated by Django 4.2.5 on 2024-01-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_tasks_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='google_calendar_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
