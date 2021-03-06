# Generated by Django 4.0 on 2022-07-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_attributevalue_product_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevalue',
            name='product_variant',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='attributes',
        ),
        migrations.AddField(
            model_name='attribute',
            name='product_variants',
            field=models.ManyToManyField(related_name='attributes', to='products.ProductVariant'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='atribute_values',
            field=models.ManyToManyField(blank=True, related_name='variants', to='products.AttributeValue'),
        ),
    ]
