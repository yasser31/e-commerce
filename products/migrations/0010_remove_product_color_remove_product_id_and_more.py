# Generated by Django 4.0 on 2022-05-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_prdouct_product_prdouct_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prdouct_color',
        ),
        migrations.CreateModel(
            name='ColorMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=265, null=True)),
                ('product_color', models.ManyToManyField(blank=True, null=True, to='products.ColorMixin')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colormixin_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.colormixin'),
            preserve_default=False,
        ),
    ]
