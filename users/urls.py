from django.contrib.auth import views as auth_views
from django.urls import include, path

from users import views as user_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]
