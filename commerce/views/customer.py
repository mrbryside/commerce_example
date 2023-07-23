from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.exception.exception_wrapper import view_exception
from utils.http.http_wrapper import response
from domain.customer.service import CustomerService
from rest_framework import status


@api_view(["POST"])
@response
@view_exception
def login(request: HttpRequest):
    customer_name = request.data.get("username")
    password = request.data.get("password")

    # get service from injector
    service: CustomerService = request.injector.get(CustomerService)
    aggregate = service.login(customerName=customer_name, password=password)
    return Response(
        {
            "auth": {
                "access_token": aggregate.auth.access_token,
                "refresh_token": aggregate.auth.refresh_token,
            },
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@response
@view_exception
def signup(request: HttpRequest):
    # get request body
    customer_name = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    # get service from injector
    service: CustomerService = request.injector.get(CustomerService)
    aggregate = service.create_customer(
        customerName=customer_name, password=password, email=email
    )

    return Response(
        {
            "customer": {
                "id": aggregate.customer.id,
                "name": aggregate.customer.name,
                "email": aggregate.customer.email,
            },
            "auth": {
                "access_token": aggregate.auth.access_token,
                "refresh_token": aggregate.auth.refresh_token,
            },
        },
        status=status.HTTP_201_CREATED,
    )
