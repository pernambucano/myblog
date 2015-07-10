# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150710_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='abstract',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
