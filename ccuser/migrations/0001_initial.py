# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('user', models.ForeignKey(to_field='id', unique=True, to=settings.AUTH_USER_MODEL)),
                ('liked_artists', models.ForeignKey(to_field='id', to='artist.Artist', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
