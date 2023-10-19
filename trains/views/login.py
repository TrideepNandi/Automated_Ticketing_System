from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):
   if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      
      user=auth.authenticate(username=username,password=password)
      
      if user is not None:
         auth.login(request,user)
         return render(request,'trains/search_train.html')
      else:
         messages.info(request,'INVALID Credentials')
         return redirect('login')
   else:
      return render(request,'trains/login.html')  
