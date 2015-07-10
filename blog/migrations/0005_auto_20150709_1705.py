# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150709_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotation',
            options={'ordering': ('URI',)},
        ),
    ]
