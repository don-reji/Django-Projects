# Generated by Django 4.2.5 on 2023-12-29 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_tasks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dependency',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.tasks'),
        ),
    ]
