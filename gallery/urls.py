from django.urls import path
from .views import *

urlpatterns = [
    path("", my_gallery, name="mygallery"),
]
