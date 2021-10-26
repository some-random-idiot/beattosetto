# Generated by Django 3.2.8 on 2021-10-22 08:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatmap_collections', '0010_auto_20211022_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_list',
            field=models.ImageField(default='collection_list/placeholder.png', upload_to='collection_list', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])]),
        ),
    ]