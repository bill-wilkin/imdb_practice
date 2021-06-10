from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('director/create', views.create_director), # Post request that creates a new director
    path('movie/create', views.create_movie),
    path('movie/<int:movie_id>', views.movie_profile),
    path('actor/create', views.create_actor),
    path('movie/<int:movie_id>/edit', views.edit_movie),
    path('movie/<int:movie_id>/update', views.update_movie),
    # Note: we are going to fix this delete lecture
    path('movie/<int:movie_id>/delete', views.delete),
]