# Generated by Django 2.1 on 2018-10-15 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit_logs',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 7, 58, 27, 498320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visit_logs',
            name='logout_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 15, 7, 58, 27, 526834, tzinfo=utc)),
        ),
    ]