# Generated by Django 3.2.8 on 2021-10-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211012_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]
