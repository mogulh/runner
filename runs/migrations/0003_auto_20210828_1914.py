# Generated by Django 3.2.6 on 2021-08-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0002_auto_20210828_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runstamp',
            name='end_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='runstamp',
            name='start_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
