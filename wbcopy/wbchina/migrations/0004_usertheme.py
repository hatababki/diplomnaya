# Generated by Django 5.2 on 2025-05-26 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbchina', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('light', 'Светлая'), ('dark', 'Темная'), ('system', 'Системная')], default='system', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тема пользователя',
                'verbose_name_plural': 'Темы пользователей',
            },
        ),
    ]
