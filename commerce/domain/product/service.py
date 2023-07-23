from typing import Dict, List
from injector import inject
from domain.product.aggregate import ProductAggregate
from domain.product.repository import ProductRepository


class ProductService:
    product_repository: ProductRepository

    @inject
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_product(
        self,
        name: str,
        brand: str,
        region: str,
        stock: int,
        price: float,
    ):
        aggregate = ProductAggregate(
            name=name,
            brand=brand,
            region=region,
            stock=stock,
            price=price,
        )

        # Receive new aggregate from inserted result
        inserted_aggregate = self.product_repository.insert_product(aggregate)

        return inserted_aggregate

    def get_all_product(self, filter_params: Dict[str, str]):
        aggregate: ProductAggregate = ProductAggregate.from_filter_only()
        for key, value in filter_params.items():
            aggregate.addItemFilter(key, value)

        product_result_aggregate = self.product_repository.get_all_product(aggregate)
        return product_result_aggregate
