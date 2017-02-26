# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moim', '0003_meeting_initialdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone_number', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moim.Meeting')),
            ],
        ),
    ]
