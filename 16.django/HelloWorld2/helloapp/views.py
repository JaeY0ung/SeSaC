from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def show_message(request):
    # DB로 부터 메세지 받아오기 (ORM 사용)
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})