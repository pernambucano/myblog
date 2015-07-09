# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('URI', models.TextField()),
                ('surfaceForm', models.TextField()),
                ('offset', models.TextField()),
                ('attributeValues', models.TextField()),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
        ),
    ]
