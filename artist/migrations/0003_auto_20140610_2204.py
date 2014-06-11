# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20140610_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='events',
            field=models.ForeignKey(null=True, blank=True, to_field='id', to='event.Event'),
        ),
    ]
