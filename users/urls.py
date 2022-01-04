from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name="list_users"),
]