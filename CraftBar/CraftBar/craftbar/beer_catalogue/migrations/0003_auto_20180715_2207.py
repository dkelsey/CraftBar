# Generated by Django 2.0.7 on 2018-07-15 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_catalogue', '0002_auto_20180715_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='type',
            new_name='beer_style',
        ),
        migrations.RemoveField(
            model_name='brewery',
            name='beer_style',
        ),
    ]
