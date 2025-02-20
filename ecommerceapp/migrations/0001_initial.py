# Generated by Django 3.2.7 on 2021-10-29 04:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=200)),
                ('model', models.CharField(max_length=250)),
                ('product_image', models.ImageField(default='default.png', upload_to='product_image/')),
                ('product_description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(1)])),
                ('in_stock', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
    ]
