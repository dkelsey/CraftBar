# Generated by Django 2.0.7 on 2018-07-15 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brewery',
            old_name='type',
            new_name='beer_style',
        ),
    ]
