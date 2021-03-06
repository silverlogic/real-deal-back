# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('copy', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='merchantoffer',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Offer'),
        ),
    ]
