from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from car_app.forms import login_form, owner_form, customer_form


# Create your views here.
def landing(request):
    return render(request,'landing.html')

def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')

def log_form(request):
    form1 =  login_form
    return render(request,"login_form.html",{"form1":form1})

def owner_add(request):
    login_form1 = login_form()
    owner_form1= owner_form()
    if request.method == 'POST':
        owner_form1 = owner_form(request.POST)
        login_form1 = login_form(request.POST)

        if owner_form1.is_valid() and login_form1.is_valid():
            owner1 = login_form1.save(commit=False)
            owner1.is_owner = True
            owner1.save()

            user = owner_form1.save(commit=False)
            user. owner_data = owner1
            user.save()
            print(user)
            return redirect('owner_add')
    return render(request,"owner/owner_form.html",{'owner_form':owner_form1,'login_form':login_form1 })

def customer_add(request):
    login_form1= login_form()
    customer_form1 = customer_form()

    if request.method == 'POST':
        customer_form1 = customer_form(request.POST)
        login_form1 = login_form(request.POST)

        if customer_form1.is_valid() and login_form1.is_valid():
            customer1 = login_form1.save(commit=False)
            customer1.is_customer = True
            customer1.save()

            user = customer_form1.save(commit=False)
            user.customer_data = customer1
            user.save()
            return redirect('customer_add')

    return render(request,'customer/customer_form.html',{'customer_form':customer_form1,'login_form':login_form1 })

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password1')
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            if user.is_staff:
                print("staff")
                return redirect('admin_dashboard')
            elif user.is_customer:
                print("cus")

                return redirect('customer_dashboard')
            elif user.is_owner:
                print("user")

                return redirect('owner_dashboard')
        else:
             messages.info(request,'Invalid Credentials')
    return render(request,'login1.html')