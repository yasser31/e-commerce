# Generated by Django 4.0 on 2022-05-04 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_category_sub_category_category_sub_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='parent',
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]