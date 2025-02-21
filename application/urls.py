from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayView.as_view(), name='display')
]