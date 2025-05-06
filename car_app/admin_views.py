from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from car_app.forms import owner_form
from car_app.models import customer, owner, vehicle

@login_required(login_url='landing')
def customer_details(request):
    data = customer.objects.all()
    return render(request,"admin/customer_details.html",{"data":data})

@login_required(login_url='landing')
def owner_details(request):
    data = owner.objects.all()
    return render(request,"admin/owner_details.html",{"data":data})

@login_required(login_url='landing')
def view_vehicle(request):
    vehicles = vehicle.objects.all()
    return render(request, "admin/view_vehicles.html", {"vehicles": vehicles})

@login_required(login_url='landing')
def delete_customer(request,id):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect("customer_details")

    return render(request,"customer_details.html")

@login_required(login_url='landing')
def delete_owner(request,id):
    data = owner.objects.get(id=id)
    data.delete()
    return redirect("owner_details")

    return render(request,"owner_details.html")

from django.shortcuts import render
from .models import pay

@login_required(login_url='landing')
def payment_history(request):
    payments = pay.objects.select_related('book__vehicle', 'book__customer').all()
    return render(request, 'admin/payment_tracking.html', {'payments': payments})
