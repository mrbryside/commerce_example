from typing import Dict
from rest_framework.response import Response
from rest_framework import status
from domain.product.aggregate import ProductAggregate
from utils.exception.exception_wrapper import view_exception
from utils.http.http_wrapper import response
from rest_framework.views import APIView
from domain.product.service import ProductService


# View for API: [POST, GET]
# path: /products
class ProductView(APIView):
    @response
    @view_exception
    def post(self, request):
        # get request body
        product_name = request.data.get("name")
        product_price = request.data.get("price")
        product_stock = request.data.get("stock")
        product_region = request.data.get("region")
        product_brand = request.data.get("brand")

        # get service from injector and init aggregate
        service: ProductService = request.injector.get(ProductService)
        created_aggregate: ProductAggregate = service.create_product(
            name=product_name,
            brand=product_brand,
            region=product_region,
            stock=product_stock,
            price=product_price,
        )

        return Response(
            {
                "id": created_aggregate.product.id,
                "name": created_aggregate.product.name,
                "brand": created_aggregate.product.brand,
                "region": created_aggregate.product.region,
                "stock": created_aggregate.product.stock,
                "price": created_aggregate.price,
            },
            status=status.HTTP_201_CREATED,
        )

    @response
    @view_exception
    def get(self, request):
        # get request query params keys, values and convert to dict
        filterParams: Dict[str, str] = {
            key: value for key, value in request.GET.items()
        }

        # get service from injector and execute get all product
        service: ProductService = request.injector.get(ProductService)
        product_result_aggregate = service.get_all_product(filterParams)

        # generate response
        product_response = [
            aggregate.toDict() for aggregate in product_result_aggregate
        ]

        return Response({"products": product_response}, status=status.HTTP_200_OK)
