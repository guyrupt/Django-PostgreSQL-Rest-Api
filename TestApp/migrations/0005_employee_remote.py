# Generated by Django 3.2.8 on 2021-11-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0004_auto_20211104_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='remote',
            field=models.BooleanField(default=False),
        ),
    ]
