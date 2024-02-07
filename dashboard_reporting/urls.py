from django.urls import path
from users.views import register

urlpatterns = [
    path('dashboard/', register, name='dashboard'),
    path('index/', register, name='index')
]
