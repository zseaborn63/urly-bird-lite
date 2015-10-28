# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0007_bookmark_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='click',
            name='click_nums',
        ),
    ]
