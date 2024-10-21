from django.urls import path
from .views import *

urlpatterns = [
    path("", contact_me, name="contactme"),
]
