# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Symbol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='poll.User')),
            ],
        ),
    ]
