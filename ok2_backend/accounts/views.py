import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
@csrf_exempt
def login_view(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                             'role': 'hak', 'email': user.email})
    else:
        return JsonResponse({'status': 401})


def logout_view(request):
    logout(request)


@csrf_exempt
def register(request):
    data = json.loads(request.body)
    # email, first_name, last_name, role, password
    user = User.objects.create_user(data['email'], data['email'], data['password'])
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.save()
    return JsonResponse({'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name,
                         'role': data['role'], 'email': user.email})


def edit_user():
    pass