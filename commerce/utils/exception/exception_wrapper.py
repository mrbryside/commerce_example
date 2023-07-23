from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


def internal_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IntegrityError as e:
            raise IntegrityError("Database integrity error: " + str(e))

        except Exception as e:
            raise ValueError("An unexpected error occurred: " + str(e))

    return wrapper


def view_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper
