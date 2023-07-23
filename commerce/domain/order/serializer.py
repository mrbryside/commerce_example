from rest_framework import serializers
from commerce.models import OrderingProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = OrderingProduct
        fields = ["id", "orderId", "quantity", "productId", "userId"]
