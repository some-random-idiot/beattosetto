# Generated by Django 3.2.8 on 2021-11-02 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='cover_list/placeholder.jpg', upload_to='cover_list', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])]),
        ),
    ]
