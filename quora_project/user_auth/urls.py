from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile_view'),
    path('update_profile_picture/', update_profile_picture, name='update_profile_picture'),

]
