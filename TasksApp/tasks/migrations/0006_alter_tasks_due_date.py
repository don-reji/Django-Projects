# Generated by Django 4.2.5 on 2023-12-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_tasks_dependency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(),
        ),
    ]