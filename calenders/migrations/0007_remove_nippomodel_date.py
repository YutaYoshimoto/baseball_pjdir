# Generated by Django 3.1 on 2022-12-10 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calenders', '0006_auto_20221211_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nippomodel',
            name='date',
        ),
    ]
