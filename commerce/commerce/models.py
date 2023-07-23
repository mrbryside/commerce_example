from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class OrderingProduct(models.Model):
    id = models.AutoField(primary_key=True)
    orderId = models.UUIDField()
    quantity = models.IntegerField()
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "ordering_products"

    def __str__(self):
        return str(self.orderId)
