from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Built-in LoginView for login page
    path('', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),

    # Built-in LogoutView (redirects to login after logout)
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Dashboard after login
    path('dashboard/', views.dashboard, name='dashboard'),

    # Add skill form page
    path('add/', views.add_skill, name='add_skill'),
]
