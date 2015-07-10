# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150709_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, serialize=False, default=None, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
