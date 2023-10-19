from django.http import HttpResponse
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from trains.forms import RegistrationForm
from django.views import View
from django.contrib.auth import login,logout,authenticate

class RegisterView(View):
  
    def get (self, request):
        r_form = RegistrationForm()
        return render(request, 'registration\login.html', {"r_form": r_form})
    
    def post (self, request):
        r_form = RegistrationForm(request.POST)    
        if r_form.is_valid():
            user = r_form.save()
            username = r_form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'Account created and logged in for {username}')
            return redirect('/search_train')
        
        else:
            return render (request, 'registration\login.html', {"r_form": r_form})
