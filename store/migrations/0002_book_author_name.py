# Generated by Django 3.2.8 on 2021-10-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
