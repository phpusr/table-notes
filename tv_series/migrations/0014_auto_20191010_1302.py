# Generated by Django 2.2.4 on 2019-10-10 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_series', '0013_auto_20191010_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tv_series.Status'),
        ),
    ]