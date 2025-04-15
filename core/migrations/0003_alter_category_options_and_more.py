# Generated by Django 4.2.20 on 2025-04-15 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'category'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor_image',
            new_name='image',
        ),
    ]
