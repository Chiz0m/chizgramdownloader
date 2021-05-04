from . import views
from django.urls import path

urlpatterns = [
    path('create', views.saveDownloadIg, name='create')
]
