# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField(blank=True)),
                ('event_name', models.CharField(blank=True, max_length=256, default='')),
                ('event_description', models.TextField()),
                ('venue_name', models.CharField(blank=True, max_length=256, default='')),
                ('venue_address', models.CharField(blank=True, max_length=256, default='')),
                ('venue_description', models.TextField()),
                ('venue_phone_number', models.CharField(blank=True, max_length=256, default='')),
                ('genre', models.CharField(blank=True, max_length=256, default='')),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
