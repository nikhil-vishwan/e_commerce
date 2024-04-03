from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from . models import Customer
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
    if request.POST and 'login' in request.POST:
        context['register']=False
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            #create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer account
            customer=Customer.objects.create(
                user=user,
                phone=phone
            )  
            success_message=" User registerd successfully"
            messages.success(request, success_message)
        except Exception as e:
            error_message="Already exsist username"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:

        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        print(user  )
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'invalid user login')

    return render(request, 'account.html', context)