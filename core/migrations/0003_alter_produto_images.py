# Generated by Django 4.2.2 on 2023-07-11 14:15

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_produto_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='images',
            field=pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, pixel_densities=[1, 2], upload_to='produtos'),
        ),
    ]