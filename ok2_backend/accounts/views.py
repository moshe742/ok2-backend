from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(user)
        return JsonResponse({'status': 200})
    else:
        return JsonResponse({'status': 401})


def logout_view(request):
    logout(request)


def register(request):
    data = request.POST.body
    # email, first_name, last_name, role, password
    user = User.objects.create_user(data['email'], data['email'], data['password'])
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.save()
    return JsonResponse(user)


def edit_user():
    pass