from django.urls import path
from physimathcode import views

urlpatterns = [
    path('',views.home,name='Home'),
]
