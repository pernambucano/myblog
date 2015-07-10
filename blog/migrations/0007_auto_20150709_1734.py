# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150709_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='p',
            field=models.ForeignKey(related_name='anotate', to='blog.Post'),
        ),
    ]
