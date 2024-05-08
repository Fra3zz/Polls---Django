from django.urls import path
from . import views

urlpatterns = [
    path("", views.cookieclass.as_view())
]
