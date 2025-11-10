from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('login/', views.NewsLoginView.as_view(), name='login'),
    path('logout/', views.NewsLogoutView.as_view(), name='logout'),
]
