# Generated by Django 2.2.1 on 2019-06-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20190609_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating_total',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating_users',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='borrow_date',
            field=models.DateField(null=True),
        ),
    ]
