from django.http import HttpResponse
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from trains.forms import RegistrationForm
from django.views import View
from django.contrib.auth import login,logout,authenticate

class RegisterView(View):
    def post (self, request):
            username = request.POST.get('username') 
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User(username = username, email = email, password = password)
            user.save()
            login(request, user)
            messages.success(request, f'Account created and logged in for {username}')
            return redirect('/search-train')

