# Generated by Django 4.0.5 on 2022-06-21 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinterests_userprofile_interests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInterests',
            new_name='UserInterest',
        ),
    ]