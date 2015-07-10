# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150709_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotation',
            old_name='attributeValues',
            new_name='label',
        ),
    ]
