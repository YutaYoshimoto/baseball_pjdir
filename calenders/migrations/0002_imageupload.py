# Generated by Django 3.1 on 2022-12-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calenders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='media_local')),
            ],
        ),
    ]
