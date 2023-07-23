import datetime
from typing import Any, Dict, List
from injector import inject
from entities.item import Item
from domain.order.aggregate import OrderAggregate

from domain.order.repository import OrderRepository


class OrderService:
    @inject
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(
        self,
        customer_id: int,
        name: str,
        place_date: datetime.datetime,
        shopping_cart: List[Dict[str, Any]],
    ) -> OrderAggregate:
        order_aggregate = OrderAggregate(
            customer_id=customer_id,
            name=name,
            place_date=place_date,
        )
        if len(shopping_cart) == 0:
            raise ValueError("shopping_cart is required")

        for product in shopping_cart:
            product_id: int | None = product.get("product_id")
            quantity: int | None = product.get("quantity")
            if product_id is not None and quantity is not None:
                item: Item = Item(id=product_id, quantity=quantity)
                order_aggregate.add_product(item=item)
            else:
                raise ValueError("product_id and quantity is required")

        inserted_order_aggregate = self.order_repository.insert_order(order_aggregate)
        return inserted_order_aggregate
