from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayView.as_view(), name='display'),
    path('create/', views.ModelStorageCreateView.as_view(), name='storage_create'),
]