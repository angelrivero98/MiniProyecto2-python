from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='users'),
    path('', views.TesisView.as_view(), name='tesis'),
    path('tesis/create', views.create_tesis, name='create_tesis'),
    path('autor/', views.postAutor, name='autor'),
    path('users/', views.get_users, name='users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete', views.delete_user),
]
