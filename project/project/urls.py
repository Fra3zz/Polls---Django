from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'cats'

urlpatterns = [
    # URLs for Cats (restricted to logged-in users)
    path('', login_required(views.CatList.as_view()), name='all'),
    path('create/', login_required(views.CatCreate.as_view()), name='cat_create'),
    path('<int:pk>/update/', login_required(views.CatUpdate.as_view()), name='cat_update'),
    path('<int:pk>/delete/', login_required(views.CatDelete.as_view()), name='cat_delete'),
    
    # URLs for Breeds (restricted to logged-in users)
    path('breeds/', login_required(views.BreedList.as_view()), name='breed_list'),
    path('breeds/create/', login_required(views.BreedCreate.as_view()), name='breed_create'),
    path('breeds/<int:pk>/update/', login_required(views.BreedUpdate.as_view()), name='breed_update'),
    path('breeds/<int:pk>/delete/', login_required(views.BreedDelete.as_view()), name='breed_delete'),
]
