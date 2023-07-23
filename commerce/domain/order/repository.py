from utils.exception.exception_wrapper import internal_exception
from domain.order.serializer import OrderSerializer
from domain.order.aggregate import OrderAggregate


class OrderRepository:
    @internal_exception
    def insert_order(self, order_aggregate: OrderAggregate):
        serializer: OrderSerializer = OrderSerializer(
            data=order_aggregate.toDictInternal(),
            many=True,
        )
        if not serializer.is_valid():
            raise ValueError(serializer.errors)

        serializer.save()
        # Insert order and add product information from saved serializer
        inserted_aggregate: OrderAggregate = OrderAggregate.from_including_id(
            order_id=order_aggregate.order.order_id,
            customer_id=order_aggregate.customer_id,
        )
        inserted_aggregate.prepare_shopping_cart(items=order_aggregate.shopping_cart)

        return inserted_aggregate
