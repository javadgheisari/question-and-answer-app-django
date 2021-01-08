from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [path('Login/', views.user_login, name='Login'),
               path('register/', views.user_register, name='register'),
               path('Logout/', views.user_logout, name='Logout'),
               path('dashboard/<int:user_id>/', views.user_dashboard, name='dashboard')]
