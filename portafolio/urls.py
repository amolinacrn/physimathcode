from django.urls import path
from .views import *

urlpatterns = [
    path("", my_portafolio, name="myportafolio"),
]
