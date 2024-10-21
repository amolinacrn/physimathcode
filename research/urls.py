from django.urls import path
from .views import *

urlpatterns = [
    path("", research_interests, name="research"),
]
