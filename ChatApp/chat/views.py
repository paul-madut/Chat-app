from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required


from . import forms

loginUrl = '/accounts/login/' 

@login_required(login_url=loginUrl)
def lobby(request):
    
    return render(request, "chat/lobby.html")