from django.shortcuts import get_object_or_404
from utils.exception.exception_wrapper import internal_exception
from entities.auth import Auth
from domain.customer.aggregate import CustomerAggregate
from rest_framework_simplejwt.tokens import RefreshToken
from domain.customer.serializers import UserSerializer
from django.contrib.auth.models import User


class CustomerRepository:
    def __generateAuthWithJwtToken(self, user: User) -> Auth:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Auth(
            password=user.password,
            access_token=access_token,
            refresh_token=refresh_token,
        )

    @internal_exception
    def insert_customer(
        self, customer_aggregate: CustomerAggregate
    ) -> CustomerAggregate:
        serializer = UserSerializer(data=customer_aggregate.toDict())
        if not serializer.is_valid():
            raise ValueError(serializer.errors)

        # Insert customer and set password with not hash
        serializer.save()
        user: User = User.objects.get(username=customer_aggregate.customer.name)
        user.set_password(customer_aggregate.auth.password)
        user.save()

        inserted_aggregate = CustomerAggregate(
            customerName=user.username,
        )
        if not inserted_aggregate.is_valid:
            ValueError(inserted_aggregate.error)

        inserted_aggregate.prepareAuth(self.__generateAuthWithJwtToken(user))
        inserted_aggregate.prepareCustomerId(user.id)
        inserted_aggregate.prepareCreate(user.password, user.email)

        return inserted_aggregate

    @internal_exception
    def login(self, customer_aggregate: CustomerAggregate) -> CustomerAggregate:
        user = get_object_or_404(User, username=customer_aggregate.customer.name)
        if not user.check_password(customer_aggregate.auth.password):
            raise ValueError("Invalid password")

        aggregate = CustomerAggregate(
            customerName=user.username,
        )
        if not aggregate.is_valid:
            ValueError(aggregate.error)

        aggregate.prepareAuth(self.__generateAuthWithJwtToken(user))

        return aggregate
