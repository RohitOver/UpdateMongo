# Generated by Django 3.2.4 on 2021-06-17 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='pswd',
        ),
    ]
