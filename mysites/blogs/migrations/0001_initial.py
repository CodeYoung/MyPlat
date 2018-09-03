# -*- coding: utf-8 -*-
# Generated by Django 2.0.2 on 2018-06-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=50)),
                ('user_id', models.IntegerField(default=1)),
                ('user_name', models.CharField(default='default name', max_length=10)),
                ('content', models.CharField(default='default content', max_length=500)),
                ('created_at', models.IntegerField(default=1514879938)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField(default=1)),
                ('user_id', models.IntegerField(default=1)),
                ('user_name', models.CharField(default='default name', max_length=10)),
                ('content', models.CharField(default='default content', max_length=500)),
                ('created_at', models.IntegerField(default=1514879938)),
            ],
        ),
    ]
