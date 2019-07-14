from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('tesis/', views.tesis,name= 'tesis'),
    path('', views.home, name='home')
]
