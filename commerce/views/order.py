import datetime
from typing import Any, Dict, List
from django.http import HttpRequest
from utils.exception.exception_wrapper import view_exception
from domain.order.service import OrderService
from utils.http.http_wrapper import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class OrderView(APIView):
    @response
    @view_exception
    def post(self, request: HttpRequest):
        # get user from request (token claims)
        user: User = request.user
        userId: int = user.id
        # get request body
        shopping_cart: List[Dict[str, Any]] = request.data.get("shopping_cart")
        if not isinstance(shopping_cart, List):
            return Response(
                {
                    "error": "shopping_cart must be a list",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_name: str = request.data.get("name")

        # get service from injector
        date_now = datetime.datetime.now()
        service: OrderService = request.injector.get(OrderService)
        order_aggregate = service.create_order(
            customer_id=userId,
            name=order_name,
            place_date=date_now,
            shopping_cart=shopping_cart,
        )
        product_dict_list = [
            {
                "product_id": product.id,
                "quantity": product.quantity,
            }
            for product in order_aggregate.shopping_cart
        ]

        return Response(
            {
                "order": {
                    "order_id": order_aggregate.order.order_id,
                    "name": order_name,
                    "place_date": date_now,
                },
                "products": product_dict_list,
            },
            status=status.HTTP_201_CREATED,
        )

    def get(request: HttpRequest):
        pass
