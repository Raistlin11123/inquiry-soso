# Generated by Django 4.1 on 2022-08-18 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_userclues_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userclues',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 18, 18, 16, 58, 965956)),
        ),
    ]
