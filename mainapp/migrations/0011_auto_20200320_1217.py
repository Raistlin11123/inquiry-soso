# Generated by Django 2.2 on 2020-03-20 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20200318_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='optional_answer',
            field=models.CharField(max_length=255, null=True, verbose_name='code'),
        ),
        migrations.AddField(
            model_name='clue',
            name='optional_question',
            field=models.CharField(max_length=255, null=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='userclues',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 20, 12, 17, 54, 899669)),
        ),
    ]
