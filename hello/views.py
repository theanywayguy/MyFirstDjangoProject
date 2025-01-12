
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello,world")

def brian(request):
    return HttpResponse("hello,brian")