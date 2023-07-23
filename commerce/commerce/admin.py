from django.contrib import admin
from .models import Product
from .models import OrderingProduct

admin.site.register(Product)
admin.site.register(OrderingProduct)
