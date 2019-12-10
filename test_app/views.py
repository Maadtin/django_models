from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json


# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
def create_user(request):
    if not request.POST:
        return JsonResponse({
            'message': 'Hijo de puta.'
        }, status=413, safe=False)

    data = request.POST

    user = User.objects.create_user(username='Pene')

    return JsonResponse(json.loads(user), safe=False)


@method_decorator(csrf_exempt, name="dispatch")
def get_user(request):
    data = request.POST

    username = data.get('username')
    user = User.objects.filter(username=username).first()

    return JsonResponse(json.loads(user), safe=False)


@method_decorator(csrf_exempt, name="dispatch")
def get_users(request):
    users = User.objects.all()
    return JsonResponse(list(users.values()), safe=False)
