# Generated by Django 3.2.8 on 2021-11-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0005_employee_remote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='company',
            field=models.ManyToManyField(blank=True, to='TestApp.Company'),
        ),
    ]