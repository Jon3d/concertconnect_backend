# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_auto_20140612_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist_name',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together=set([('name', 'genre')]),
        ),
    ]
