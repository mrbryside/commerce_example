import copy
from typing import Dict, Any
from dataclasses import dataclass
from entities.customer import Customer
from entities.auth import Auth


@dataclass
class CustomerAggregate:
    is_valid: bool = False
    error: ValueError = ValueError()

    def __init__(self, customerName: str):
        if customerName == "":
            self.is_valid = True
            self.error = ValueError("failed, from init customer aggregate")

        self.__customer: Customer = Customer(
            name=customerName,
        )
        self.__auth: Auth = Auth()

    # -- all property getter -- #
    @property
    def customer(self):
        return copy.deepcopy(self.__customer)

    @property
    def auth(self):
        return copy.deepcopy(self.__auth)

    # -- business domain functional -- #
    def prepareAuth(self, auth: Auth):
        self.__auth = auth

    def prepareCustomerId(self, id: int):
        self.__customer.id = id

    def prepareCreate(self, password: str, email: str):
        self.__customer.email = email

    # -- serializer -- #
    def toDict(self) -> Dict[str, Any]:
        return {
            "id": self.__customer.id,
            "username": self.__customer.name,
            "password": self.__auth.password,
            "email": self.__customer.email,
        }
