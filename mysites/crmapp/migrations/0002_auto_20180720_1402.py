# Generated by Django 2.0.2 on 2018-07-20 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followrecord',
            name='RecordUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]