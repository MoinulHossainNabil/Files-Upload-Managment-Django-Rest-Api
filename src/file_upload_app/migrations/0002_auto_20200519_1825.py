# Generated by Django 3.0.5 on 2020-05-19 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SingleFileUpload',
            new_name='FileModel',
        ),
    ]
