from django.urls import path
from .views import home, register, create_post, post_list

urlpatterns = [
    path('', home, name='home'),  # Home page at root URL
    path('register/', register, name='register'),  # Registration page
    path('create_post/', create_post, name='create_post'),  # Create post
    path('posts/', post_list, name='post_list'),  # List of posts
]

from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Login page
]

from django.urls import path
from .views import login_view  # Ensure this matches the function name in views.py

urlpatterns = [
    path('login/', login_view, name='login'),  # Add this line
    # Other URL patterns...
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
