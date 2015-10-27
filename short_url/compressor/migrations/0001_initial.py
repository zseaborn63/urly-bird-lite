# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=150)),
                ('redirect_url', models.CharField(max_length=150)),
                ('short_url', models.CharField(max_length=50)),
                ('click_nums', models.PositiveIntegerField()),
            ],
        ),
    ]
