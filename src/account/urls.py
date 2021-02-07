from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [path('Login/', views.user_login, name='Login'),
               path('register/', views.user_register, name='register'),
               path('Logout/', views.user_logout, name='Logout'),
               path('dashboard/<int:user_id>/', views.user_dashboard, name='dashboard'),
               path('all_account/', views.all_account, name='all_account'),
               path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
               path('user_delete/<int:user_id>', views.user_delete, name='user_delete')]
