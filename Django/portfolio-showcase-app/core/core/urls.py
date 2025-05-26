from django.contrib import admin
from django.urls import path, include
from . import  *

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),
]