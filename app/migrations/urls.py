from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Include app URLs
]

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
]