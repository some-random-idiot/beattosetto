# Generated by Django 3.2.8 on 2021-11-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionlog',
            name='log',
            field=models.FileField(blank=True, null=True, upload_to='actions_logs'),
        ),
    ]