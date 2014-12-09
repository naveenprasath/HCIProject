# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bwf', '0004_friendship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creditor', models.EmailField(max_length=75)),
                ('debtor', models.EmailField(max_length=75)),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=40, blank=True)),
                ('bill_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Debt',
        ),
    ]
