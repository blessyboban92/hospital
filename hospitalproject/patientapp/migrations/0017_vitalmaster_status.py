# Generated by Django 3.2.22 on 2023-11-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0016_delete_vitalinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitalmaster',
            name='status',
            field=models.CharField(default='Not Saved', max_length=255),
        ),
    ]
