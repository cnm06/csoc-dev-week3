# Generated by Django 2.2.1 on 2019-06-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20190614_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
