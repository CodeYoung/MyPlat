# Generated by Django 2.0.2 on 2018-04-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Code', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=11, null=True)),
                ('ManagersID', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500, null=True)),
                ('CreateTime', models.DateTimeField()),
                ('ModifyTime', models.DateTimeField()),
                ('Remark', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Code', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('IDCard', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=11)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('WeChat', models.CharField(max_length=100, null=True)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=10)),
                ('FingerPrint', models.CharField(max_length=1000, null=True)),
                ('PassWord', models.CharField(max_length=18)),
                ('CreateTime', models.DateTimeField()),
                ('LastLogTime', models.DateTimeField()),
                ('IsForbidden', models.BooleanField()),
                ('Remark', models.CharField(max_length=1000, null=True)),
                ('Dept', models.ForeignKey(null=True, on_delete=True, to='basemodel.Dept')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
               # ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Code', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=11, null=True)),
                ('ManagersID', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500, null=True)),
                ('CreateTime', models.DateTimeField()),
                ('ModifyTime', models.DateTimeField()),
                ('Remark', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctors',
            name='Organization',
            field=models.ForeignKey(null=True, on_delete=True, to='basemodel.Organization'),
        ),
    ]