from django.urls import path
from .views import get_csrf

urlpatterns = [
    path('csrf/', get_csrf),
]
