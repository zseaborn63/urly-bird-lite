# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0005_auto_20151027_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='long_url',
            field=models.URLField(),
        ),
    ]
