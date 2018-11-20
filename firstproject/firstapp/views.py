from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    user=request.user
    print(user)
    msg=datetime.now()
    s="<h1>Hello dheeraj welcome to your first django application</h1>"
    msg=s+"<h1>and the time date like this:"+str(msg)+"</h1>"
    return HttpResponse(msg)
