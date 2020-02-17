from django.shortcuts import render


# Create your views here.
def get_csrf(request):
    return get_token()
