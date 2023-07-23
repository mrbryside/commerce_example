from rest_framework import serializers
from commerce.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ["id", "name", "brand", "region", "stock", "price"]
