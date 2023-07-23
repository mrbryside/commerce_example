from django.core.management.base import BaseCommand
import requests
from commerce.models import Product


class Command(BaseCommand):
    help = "Seeds the database with dummy api"
    API_URL = "https://dummyjson.com/products"

    def handle(self, *args, **kwargs):
        response = requests.get(self.API_URL)

        if response.status_code == 200:
            data = response.json()
            products = data.get("products", [])

            for product in products:
                obj = Product.objects.create(
                    name=product["title"],
                    brand=product["brand"],
                    region="Thailand",
                    stock=product["stock"],
                    price=product["price"],
                )
                self.stdout.write(self.style.SUCCESS(f"Successfully saved {obj}"))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch data from the API"))
