import unittest
from domain.customer.repository import CustomerRepository
from domain.customer.serializers import UserSerializer
from domain.customer.service import CustomerService
from django.contrib.auth.models import User


class Test_Service(unittest.TestCase):
    pass
    # def test_create_customer(self):
    #     repo = Repository(UserSerializer)
    #     service = Service(repo)
    #     service.create_customer("test", "test", "test@mail.com")
