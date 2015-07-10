# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150710_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='abstract',
            field=models.TextField(),
        ),
    ]
