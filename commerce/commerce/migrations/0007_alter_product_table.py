# Generated by Django 4.2.3 on 2023-07-23 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_alter_orderingproduct_table_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]