# Generated by Django 3.2.2 on 2021-06-30 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='IC',
            new_name='ic',
        ),
    ]