from typing import Dict, Any
from rest_framework.response import Response
from rest_framework import status


def response(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        stat = False
        if (
            results.status_code == status.HTTP_200_OK
            or results.status_code == status.HTTP_201_CREATED
        ):
            stat = True
        return Response(
            {
                "success": stat,
                "content": results.data,
            },
            status=results.status_code,
        )

    return wrapper
