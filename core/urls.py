from django.urls import path

from .views import create_department, get_department, delete_department, update_department

urlpatterns = [
    path('create_department/', create_department, name='create_department'),
    path('get_department/<str:code>/', get_department, name='get_department'),
    path('delete_department/<str:code>/', delete_department, name='delete_department'),
    path('update_department/<str:code>/',update_department, name = 'delete_department')
]