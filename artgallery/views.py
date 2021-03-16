from django.shortcuts import render,redirect
from artgallery.forms import *
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from artgallery.models import *

# Create your views here.
def home(request):
    return render(request, 'artgallery/base.html', {})

def register(request):
    return render(request,'artgallery/register.html')

@login_required
def customerLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def registerCustomer(request):
    registered=False
    if request.method=='POST':
        var_customerForm=customerForm(request.POST)
        if var_customerForm.is_valid():
            customerprimary=var_customerForm.save()
            customerprimary.set_password(customerprimary.password)
            customerprimary.save()
            registered=True
            # return redirect('userLogin')
    else:
        var_customerForm=customerForm()
    return render(request,'artgallery/customerreg.html',{'var_customerForm':var_customerForm,'registered':registered})

def customerLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('customerdetail'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('registercustomer')
    else:
        return render(request,'artgallery/customerlogin.html',{'invalidlogin':invalidlogin})

def customisedproduct(request):
    if request.method == "POST":
        form = custproduct(request.POST)
        if form.is_valid():
            cuspro = form.save(commit=False)
            cuspro.save()
            return redirect('home')
    else:
        form = custproduct()

    return render(request, 'artgallery/customisedproduct.html', {'form': form})

def customerdetail(request):
    if request.method == "POST":
        form = customerdetailform(request.POST)
        if form.is_valid():
            cus = form.save(commit=False)
            cus.save()
            return redirect('customisedproduct')
    else:
        form = customerdetailform()

    return render(request, 'artgallery/customerdetail.html', {'form': form})

def adminLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('orderlist'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('home')
    else:
        return render(request,'artgallery/adminlogin.html',{'invalidlogin':invalidlogin})

def orderlist(request):
    order_list=Custpro.objects.all()
    context={'cust':order_list}
    return render(request,'artgallery/orderlist.html',context)
