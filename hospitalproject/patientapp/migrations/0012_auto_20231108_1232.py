# Generated by Django 3.2.22 on 2023-11-08 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0011_brandmaster_categorymaster_itemmaster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmaster',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='itemmaster',
            name='category',
        ),
        migrations.DeleteModel(
            name='BrandMaster',
        ),
        migrations.DeleteModel(
            name='CategoryMaster',
        ),
        migrations.DeleteModel(
            name='ItemMaster',
        ),
    ]
