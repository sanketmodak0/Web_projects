# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('subscription_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='None', max_length=100)),
                ('mobile_no', models.IntegerField(default=0)),
                ('address', models.CharField(default='None', max_length=1000)),
                ('subscription', models.IntegerField(default=0)),
                ('source_of_knowledge', models.CharField(blank=True, default='None', max_length=1000, null=True)),
                ('medical_condition', models.CharField(default='None', max_length=1000)),
                ('created_on', models.DateTimeField(default='9999-12-31 23:59:59')),
                ('updated_on', models.DateTimeField(default='9999-12-31 23:59:59')),
            ],
        ),
    ]
