# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0003_auto_20151027_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='redirect_url',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
