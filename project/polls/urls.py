from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.index.as_view(), name="main"),
    path('<int:question_id>/', views.detail.as_view(), name='detail'),
    path('<int:question_id>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote.as_view(), name='vote'),
    path("owner/", views.owner, name="Owner"),
    path("cookie/", views.cookie_jar.as_view(), name="cookie Jar"),
    path("remove_cookie/", views.rmcookie.as_view(), name="remove cookie"),
]
