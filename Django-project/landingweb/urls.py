from django.urls import path
from .views import homepage

urlpatterns: list = [
    path('', homepage, name='homepage')
]