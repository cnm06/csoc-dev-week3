# Generated by Django 2.2.1 on 2019-06-09 19:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190607_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='borrow_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 9, 19, 57, 52, 471760), null=True),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_rating', models.IntegerField()),
                ('total_users', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Book')),
            ],
        ),
    ]
