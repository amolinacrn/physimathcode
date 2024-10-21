from django.urls import path
from .views import *

urlpatterns = [
    path("", biography_information, name="biography"),
]
