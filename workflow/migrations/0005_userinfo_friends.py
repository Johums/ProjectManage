# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_userinfo_friends_+', to='workflow.UserInfo'),
        ),
    ]
