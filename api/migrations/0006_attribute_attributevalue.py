# Generated by Django 4.1.4 on 2023-08-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_product_description_alter_productline_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='attributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.attribute')),
            ],
        ),
    ]