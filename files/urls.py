from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='files-index'),
    path('upload/', views.upload_view, name='files-upload'),
]