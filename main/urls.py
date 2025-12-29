# main/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
]