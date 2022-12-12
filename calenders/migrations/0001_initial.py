# Generated by Django 3.1 on 2022-12-12 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default-title', max_length=100)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='NippoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='日付')),
                ('team', models.CharField(default='チーム名', max_length=100, verbose_name='チーム名')),
                ('district', models.CharField(default='地区', max_length=100, verbose_name='地区')),
                ('content', models.TextField(default='default-content', verbose_name='内容')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
