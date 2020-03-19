# Generated by Django 3.0.4 on 2020-03-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20200316_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'Didnt Read'), (2, 'Reading'), (3, 'Done'), (4, 'Stopped')], default=1),
        ),
    ]
