# Generated by Django 4.1.4 on 2023-08-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productline',
            name='attributeValue',
            field=models.ManyToManyField(blank=True, related_name='attributeValue', to='api.attributevalue'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='api.category'),
        ),
    ]
