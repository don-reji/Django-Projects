# Generated by Django 4.2.5 on 2023-12-28 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_dependency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='dependency',
        ),
    ]