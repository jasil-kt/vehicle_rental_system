from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from car_app.filters import BrandFilter
from car_app.models import vehicle, customer, book_now


def customer_dashboard(request):
    return render(request,'customer/customer_dashboard.html')

def vehicle_view(request):
    data = vehicle.objects.all()
    brand_filter = BrandFilter(request.GET,queryset=data)
    data = brand_filter.qs

    return render(request,"customer/view.html",{"data":data,"brand_filter":brand_filter})

def book_vehicle(request, id):
    vehicle_data = vehicle.objects.get(id=id)

    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        customer_data1 =customer.objects.get(customer_data=request.user)
        days_rented = (end_date - start_date).days
        total_price = days_rented * float(vehicle_data.price_per_day)
        booking = book_now.objects.create(
            vehicle=vehicle_data,
            customer=customer_data1,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            status=0
        )

        messages.success(request, "Vehicle booked successfully! Pending approval.")
        return redirect("customer_dashboard")

    return render(request, "customer/book_vehicle.html", {"vehicle": vehicle_data})