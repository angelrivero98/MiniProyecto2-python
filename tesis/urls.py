from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update', views.update_user, name='update_user'),
    path('users', views.get_users),
    path('users/<int:user_id>/delete', views.delete_user),
    path('tesis/', views.tesis,name= 'tesis'),
]
