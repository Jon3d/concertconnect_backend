# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('artist_name', models.CharField(max_length=256, default='', blank=True)),
                ('artist_label', models.CharField(max_length=256, default='', blank=True)),
                ('bio', models.TextField()),
                ('currently_touring', models.BooleanField(default=False)),
                ('country_of_origin', models.CharField(max_length=256, default='', blank=True)),
                ('genre', models.CharField(max_length=256, default='', blank=True)),
                ('events', models.ForeignKey(to_field='id', to='event.Event')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
