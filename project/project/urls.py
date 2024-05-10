from django.urls import path, include
from django.contrib import admin  # Import admin module

app_name = 'cats'

urlpatterns = [
    path("admin/", admin.site.urls),  # Include admin URLs
    path("", include("home.urls")),
    path("hello/", include("hello.urls")),
    path("autos/", include("autos.urls")),
    path("cats/", include("cats.urls")),
    path("polls/", include("polls.urls"))
]