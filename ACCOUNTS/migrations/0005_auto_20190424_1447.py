# Generated by Django 2.1.3 on 2019-04-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0004_auto_20190423_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
