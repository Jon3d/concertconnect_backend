# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '__first__'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedArtist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tag', models.ForeignKey(to='taggit.Tag', to_field='id')),
                ('content_object', models.ForeignKey(to='artist.Artist', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='mbid',
            field=models.CharField(default='', max_length=256, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='similar_artists',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to=taggit.models.Tag, through=taggit.models.TaggedItem, verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
