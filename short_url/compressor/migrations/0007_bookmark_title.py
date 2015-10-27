# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0006_auto_20151027_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=25, default=None),
            preserve_default=False,
        ),
    ]
