import unittest
from domain.product.repository import ProductRepository
from domain.product.service import ProductService


class Test_Service(unittest.TestCase):
    def test_create_product(self):
        repo = ProductRepository()
        service = ProductService(repo)
        service.create_product(
            name="oh name", brand="oh brand", region="oh region", stock=1, price=1.0
        )
