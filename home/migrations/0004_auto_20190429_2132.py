# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190429_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home_teacher_record',
            old_name='teacher_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='home_teacher_record',
            old_name='teacher_password',
            new_name='password',
        ),
    ]
