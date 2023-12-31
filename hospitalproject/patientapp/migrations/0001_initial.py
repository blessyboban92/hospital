# Generated by Django 3.2.22 on 2023-10-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientid', models.CharField(max_length=15)),
                ('patientname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('mobile1', models.CharField(max_length=12)),
                ('mobile2', models.CharField(max_length=12)),
            ],
        ),
    ]
