from django.http import HttpResponseForbidden
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.deprecation import MiddlewareMixin
from django.core.handlers.wsgi import WSGIRequest
from injector import Injector
from .injector import configure


class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth = JWTAuthentication()

        try:
            auth_header = request.headers.get("Authorization")
            if auth_header is None or not auth_header.startswith("Bearer "):
                return HttpResponseForbidden("Invalid token")

            token = auth_header.split(" ")[1]
            validated_token = auth.get_validated_token(token)
            user = auth.get_user(validated_token)
            request.user = user
        except Exception:
            return HttpResponseForbidden("Invalid token")

        return self.get_response(request)


class InjectorMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.injector = Injector([configure])
        super().__init__(get_response)

    def process_request(self, request: WSGIRequest):
        request.injector = self.injector


from django.utils.deprecation import MiddlewareMixin


class DisableCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, "_dont_enforce_csrf_checks", True)
