# Generated by Django 2.0 on 2018-09-26 09:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20180926_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit_log',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 9, 15, 36, 485591, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visit_log',
            name='logout_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 9, 15, 36, 604309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='phone_number',
            field=models.CharField(default='0912345678', max_length=10),
        ),
    ]