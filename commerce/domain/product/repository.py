from typing import List
from injector import inject
from commerce.models import Product
from utils.exception.exception_wrapper import internal_exception
from domain.product.aggregate import ProductAggregate
from domain.product.serializer import ProductSerializer


class ProductRepository:
    @internal_exception
    def insert_product(self, product_aggregate: ProductAggregate) -> ProductAggregate:
        serializer: ProductSerializer = ProductSerializer(
            data=product_aggregate.toDict()
        )
        if not serializer.is_valid():
            raise ValueError(serializer.errors)

        serializer.save()
        # Insert customer and set password with not hash
        inserted_aggregate: ProductAggregate = ProductAggregate.from_including_id(
            id=serializer.data["id"],
            name=serializer.data["name"],
            brand=serializer.data["brand"],
            region=serializer.data["region"],
            stock=serializer.data["stock"],
            price=serializer.data["price"],
        )

        return inserted_aggregate

    @internal_exception
    def get_all_product(
        self, product_aggregate: ProductAggregate
    ) -> List[ProductAggregate]:
        filter_conditions = {
            f"{key}__icontains": value
            for key, value in product_aggregate.product_filter.items()
        }
        products = Product.objects.filter(**filter_conditions)
        product_result_aggregate: List[ProductAggregate] = [
            ProductAggregate.from_including_id(
                id=product.id,
                name=product.name,
                brand=product.brand,
                region=product.region,
                stock=product.stock,
                price=product.price,
            )
            for product in products
        ]

        return product_result_aggregate
