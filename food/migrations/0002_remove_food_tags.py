# Generated by Django 3.2.5 on 2022-06-14 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='tags',
        ),
    ]
