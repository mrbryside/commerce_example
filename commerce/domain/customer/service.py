from injector import inject
from entities.auth import Auth
from domain.customer.aggregate import CustomerAggregate
from domain.customer.repository import CustomerRepository


class CustomerService:
    customer_repository: CustomerRepository

    @inject
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def create_customer(
        self, customerName: str, password: str, email: str
    ) -> CustomerAggregate:
        # Init entity and aggregate and create customer
        auth = Auth(password=password)
        aggregate = CustomerAggregate(customerName)
        aggregate.prepareAuth(auth)
        aggregate.prepareCreate(password=password, email=email)

        # Receive new aggregate from inserted result
        inserted_aggregate = self.customer_repository.insert_customer(aggregate)

        return inserted_aggregate

    def login(self, customerName: str, password: str) -> CustomerAggregate:
        # Init entity and aggregate and create customer
        auth = Auth(password=password)
        aggregate = CustomerAggregate(customerName)
        aggregate.prepareAuth(auth)

        # Receive new aggregate from inserted result
        inserted_aggregate = self.customer_repository.login(aggregate)

        return inserted_aggregate
