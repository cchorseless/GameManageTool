from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,template_name='login.html')