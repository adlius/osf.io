# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 19:54
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import osf.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0036_merge'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='osfuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='abstractnode',
            name='date_created',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='abstractnode',
            name='date_modified',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractnode',
            name='deleted_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abstractnode',
            name='forked_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='apioauth2application',
            name='date_created',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='archivejob',
            name='datetime_initiated',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now, verbose_name=b'initiated at'),
        ),
        migrations.AlterField(
            model_name='citationstyle',
            name='date_parsed',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_modified',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='externalaccount',
            name='date_last_refreshed',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='externalaccount',
            name='expires_at',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fileversion',
            name='date_created',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fileversion',
            name='date_modified',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='guid',
            name='created',
            field=osf.utils.fields.NonNaiveDateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='nodelog',
            name='date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='notificationdigest',
            name='timestamp',
            field=osf.utils.fields.NonNaiveDateTimeField(),
        ),
        migrations.AlterField(
            model_name='preprintservice',
            name='date_created',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='preprintservice',
            name='date_modified',
            field=osf.utils.fields.NonNaiveDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='preprintservice',
            name='date_published',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storedfilenode',
            name='last_touched',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trashedfilenode',
            name='deleted_on',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='trashedfilenode',
            name='last_touched',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
        migrations.AlterIndexTogether(
            name='guid',
            index_together=set([('content_type', 'object_id', 'created')]),
        ),
        migrations.AlterIndexTogether(
            name='noderelation',
            index_together=set([('is_node_link', 'child', 'parent')]),
        ),
    ]