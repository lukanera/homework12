# Generated by Django 5.1.4 on 2024-12-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sort',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
