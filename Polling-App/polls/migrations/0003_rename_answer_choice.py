# Generated by Django 4.2.5 on 2023-10-13 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Choice',
        ),
    ]
