# Generated by Django 4.0 on 2022-07-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='product_variant',
            field=models.ManyToManyField(blank=True, related_name='attr_values', to='products.ProductVariant'),
        ),
    ]
