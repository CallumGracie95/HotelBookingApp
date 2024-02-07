from django.urls import path
from .views import register, user_login  # Ensure you import the correct view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),  # Corrected to point to user_login view
]
