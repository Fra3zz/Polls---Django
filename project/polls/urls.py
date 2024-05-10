from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.Index.as_view(), name="main"),
    path('<int:question_id>/', views.Detail.as_view(), name='detail'),
    path('<int:question_id>/results/', views.Results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.Vote.as_view(), name='vote'),
    path("owner/", views.Owner.as_view(), name="Owner"),
    path("cookie/", views.CookieJar.as_view(), name="cookie Jar"),
    path("remove_cookie/", views.RemoveCookie.as_view(), name="remove cookie"),
]