from django.urls import path
from . import views

urlpatterns = [
    path("cookie/", views.cookie, name="cookie"),  # Include URL for function-based view
    path("cookieclass/", views.cookieclass.as_view(), name="cookieclass"),  # Include URL for class-based view
]
