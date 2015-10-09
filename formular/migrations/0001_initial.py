# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=4, choices=[[b'test', b'Testing'], [b'dev', b'Development'], [b'prod', b'Production']])),
            ],
        ),
        migrations.CreateModel(
            name='Proposal2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ongoing_projects', models.CharField(max_length=1000)),
                ('past_projects', models.CharField(max_length=1000)),
                ('editing_styles', models.CharField(max_length=5, choices=[[b'plain', b'Plain text'], [b'latex', b'Latex']])),
            ],
        ),
    ]
