from django.urls import path
from .views import *

urlpatterns = [
    path("", show_publications, name="publications"),
]
