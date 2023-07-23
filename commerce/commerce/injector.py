# injector.py

from injector import Binder, singleton
from domain.order.repository import OrderRepository
from domain.order.service import OrderService
from domain.product.repository import ProductRepository
from domain.product.service import ProductService
from domain.customer.repository import CustomerRepository
from domain.customer.service import CustomerService


def configure(binder: Binder) -> Binder:
    # Service
    binder.bind(CustomerService, to=CustomerService, scope=singleton)
    binder.bind(ProductService, to=ProductService, scope=singleton)
    binder.bind(OrderService, to=OrderService, scope=singleton)
    # Repository
    binder.bind(ProductRepository, to=ProductRepository, scope=singleton)
    binder.bind(CustomerRepository, to=CustomerRepository, scope=singleton)
    binder.bind(OrderRepository, to=OrderRepository, scope=singleton)

    return binder
