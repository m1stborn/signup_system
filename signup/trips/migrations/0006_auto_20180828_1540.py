# Generated by Django 2.0 on 2018-08-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20180827_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='path/', verbose_name='Label')),
            ],
        ),
        migrations.AlterField(
            model_name='visitor',
            name='signature',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]
