"""
URL configuration for commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from commerce.middleware import TokenValidationMiddleware
from views.order import OrderView
from views.product import ProductView
from views import customer
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", customer.login),
    path("signup", customer.signup),
    # protected endpoint
    path(
        "products",
        TokenValidationMiddleware(ProductView.as_view()),
        name="products",
    ),
    path(
        "orders",
        TokenValidationMiddleware(OrderView.as_view()),
        name="orders",
    ),
]
