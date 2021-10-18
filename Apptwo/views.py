from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':  "Hello I am from views.py!"}
    return render(request, 'Apptwo/index.html',context=my_dict)

def help(request):
    return render(request,"Apptwo/help.html")