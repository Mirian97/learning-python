# Generated by Django 5.1.4 on 2024-12-30 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image_product_name_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(max_length=255, null=True)),
                ('discount', models.FloatField(default=0)),
            ],
        ),
    ]
