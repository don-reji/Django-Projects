# Generated by Django 4.2.5 on 2023-12-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dependency',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.tasks'),
        ),
    ]
