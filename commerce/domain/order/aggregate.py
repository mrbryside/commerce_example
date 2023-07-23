import copy
import datetime
from typing import Any, Dict, List
import uuid
from entities.order import Order
from entities.item import Item


class OrderAggregate:
    def __init__(
        self, customer_id: int, name: str, place_date: datetime.datetime
    ) -> None:
        self.__shopping_cart: List[Item] = []
        self.__order: Order = Order(
            order_id=uuid.uuid4(), name=name, place_date=place_date
        )
        self.__customer_id: int = customer_id

    @classmethod
    def from_including_id(
        cls,
        customer_id: int,
        order_id: uuid.UUID,
    ) -> "OrderAggregate":
        instance = cls.__new__(cls)
        instance.__shopping_cart = []
        instance.__order = Order(
            order_id=order_id,
        )
        instance.__customer_id = customer_id
        return instance

    # ---- property method ----#
    @property
    def shopping_cart(self) -> List[Item]:
        return copy.deepcopy(self.__shopping_cart)

    @property
    def customer_id(self) -> int:
        return copy.deepcopy(self.__customer_id)

    @property
    def order(self) -> Order:
        return copy.deepcopy(self.__order)

    # ---- business method ----#
    def add_product(self, item: Item) -> None:
        self.__shopping_cart.append(item)

    def prepare_shopping_cart(self, items: List[Item]) -> None:
        self.__shopping_cart = items

    # ---- serializer ----#
    def toDictInternal(
        self,
    ) -> List[Dict[str, Any]]:
        return [
            {
                "quantity": product.quantity,
                "orderId": self.__order.order_id,
                "userId": self.__customer_id,
                "productId": product.id,
            }
            for product in self.shopping_cart
        ]
