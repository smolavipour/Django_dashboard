from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_table, name='main_page'),
]