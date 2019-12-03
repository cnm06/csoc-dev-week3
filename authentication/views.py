from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def loginView(request):
    template_path = "authentication/login.html"
    context = {}

    return render(request, template_path, context)


def logoutView(request):
    template_path = "authentication/logout.html"
    context = {}
    logout(request)
    return render(request, template_path, context)


def registerView(request):
    template_path = "authentication/register.html"
    context = {}
    return render(request, template_path, context)


@csrf_exempt
def loginlogicView(request):
    response_data = {
        'message': "failiure",
    }
    username = request.POST['username']
    password = request.POST['password']
    try:
        loginit = authenticate(username=username, password=password)
        login(request, loginit)
        response_data['message'] = 1
    except:
        pass
    return JsonResponse(response_data)


@csrf_exempt
def registerlogicView(request):
    response_data = {
        'message': "failiure",
    }
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username, '', password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        loginit = authenticate(username=username, password=password)
        login(request, loginit)
        response_data['message'] = 1
    except:
        pass
    return JsonResponse(response_data)
