# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0003_auto_20140610_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='TaggedArtist',
        ),
    ]
