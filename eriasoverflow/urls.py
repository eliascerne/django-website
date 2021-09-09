from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='eriasoverflow-home'),
    path('about/', views.about, name='eriasoverflow-about'),
]
