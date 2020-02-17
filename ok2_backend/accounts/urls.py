from django.urls import path
from accounts.views import login_view, logout_view, register, edit_user

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register),
    path('edit_user/', edit_user),
]
