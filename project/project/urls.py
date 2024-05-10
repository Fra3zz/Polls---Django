from django.urls import path, include

app_name = 'cats'

urlpatterns = [
    path("", include("home.urls")),
    path("hello/", include("hello.urls")),
    path("autos/", include("autos.urls")),
    path("cats/", include("cats.urls")),
    path("polls/", include("polls.urls"))


]