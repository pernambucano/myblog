# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_annotation_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='abstract',
            field=models.TextField(max_length=200),
        ),
    ]
