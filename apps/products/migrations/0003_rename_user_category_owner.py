# Generated by Django 4.2 on 2024-10-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_image_remove_product_image_category_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='user',
            new_name='owner',
        ),
    ]
