# Generated by Django 3.2.6 on 2021-08-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0004_auto_20210828_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runstamp',
            name='end_at',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='runstamp',
            name='start_at',
            field=models.PositiveIntegerField(),
        ),
    ]
