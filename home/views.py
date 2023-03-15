from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home/welcome.html',{})

def test(request):
    return HttpResponse('it works')


def index(request):
    return HttpResponse('Index')

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html',{})