from django.urls import path
from . import views

urlpatterns = [
    path('tesis/', views.TesisView.as_view(),name= 'tesis'),
    path('postAutor/', views.postAutor, name='postAutor'),
    path('users/', views.get_users, name='users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update', views.update_user, name='update_user'),
    path('users', views.get_users),
    path('users/<int:user_id>/delete', views.delete_user),
]
