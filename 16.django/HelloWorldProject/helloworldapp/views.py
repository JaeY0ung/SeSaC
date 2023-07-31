from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

def login_view(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            print('로그인 성공')
            login(request, user)
            return redirect('home')
        else:
            print('로그인 실패')
    return render(request, 'login.html')


@login_required
def home_view(request):
    #? 로그인한 사용자 정보
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
