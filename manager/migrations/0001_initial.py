# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30, unique=True)),
                ('enough', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['item_name'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_product', models.FloatField(default=0.0)),
                ('price_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Category')),
                ('price_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['store_name'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='category_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Store'),
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together=set([('price_category', 'price_product', 'cost_product')]),
        ),
    ]
