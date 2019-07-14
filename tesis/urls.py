from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('users/<int:id>', views.UsersView.as_view()),
    path('users/<int:user_id>/delete', views.delete_user),
    path('tesis/', views.tesis,name= 'tesis'),
    path('', views.home, name='home')
]
