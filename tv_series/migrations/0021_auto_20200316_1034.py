# Generated by Django 3.0.1 on 2020-03-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_series', '0020_auto_20191015_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]