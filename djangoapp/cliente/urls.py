from django.urls import path, include
from cliente.views import ClienteCreateView


app_name = 'cliente'


urlpatterns = [
    path('create',ClienteCreateView.as_view(), name='create'),
    
]
