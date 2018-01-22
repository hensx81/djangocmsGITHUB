# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=60, default='', choices=[('x', 'Male'), ('y', 'Female')], verbose_name='gender')),
            ],
        ),
    ]
