# Generated by Django 4.2.5 on 2023-12-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('dependency', models.ManyToManyField(blank=True, to='tasks.tasks')),
            ],
        ),
    ]
