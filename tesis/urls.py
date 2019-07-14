from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('tesis/', views.TesisView.as_view(),name= 'tesis'),
    path('postAutor/', views.postAutor, name='postAutor'),
    path('', views.home, name='home')
]
