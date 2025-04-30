from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.timezone import now

from car_app.filters import BrandFilter
from car_app.forms import payment_form
from car_app.models import vehicle, customer, book_now, pay


def customer_dashboard(request):
    return render(request,'customer/customer_dashboard.html')

def vehicle_view(request):
    data = vehicle.objects.all()


    for v in data:
        last_booking = book_now.objects.filter(vehicle=v).order_by('-end_date').first()
        if last_booking:
            if last_booking.end_date < now().date():
                v.available = True
            else:
                v.available = False
            v.save()
    data = vehicle.objects.filter(available=True)
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
        return redirect("booking_summary")

    return render(request, "customer/book_vehicle.html", {"vehicle": vehicle_data})


from django.shortcuts import render
from .models import book_now


def booking_summary(request):
    user = request.user
    customer_data1 = customer.objects.get(customer_data=user)
    data = book_now.objects.filter(customer=customer_data1)
    for booking in data:
        days_rented = (booking.end_date - booking.start_date).days
        booking.total_price = float(booking.vehicle.price_per_day) * days_rented
    return render(request, "customer/booking_summary.html", {"data": data, "customer_data": customer_data1})


def cancel_booking(request,id):
    booking = book_now.objects.get(id=id)
    if booking.status == 0:
        booking.delete()
        booking.vehicle.available = True
        booking.vehicle.save()
    messages.success(request, "Booking has been canceled successfully.")
    return redirect("customer_dashboard")
    return render(request,"customer/booking_summary.html")

def pay_now(request,id):
    booking = book_now.objects.get(id=id)
    if request.method == "POST":
        form = payment_form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.book = booking
            obj.save()
            booking.status = 1
            booking.save()
            booking.vehicle.available = False
            booking.vehicle.save()
            return redirect("payment_view")
    else:
        form = payment_form()

    return render(request, "customer/payment_page.html", {"form": form, "booking": booking})

from django.shortcuts import render
from .models import pay, customer

def payment_tracking(request):
    user = request.user
    try:
        customer_data = customer.objects.get(customer_data=user)
    except customer.DoesNotExist:
        return render(request, "customer/payment_tracking.html", {"error": "Customer data not found."})

    payments = pay.objects.filter(book__customer=customer_data).select_related("book__vehicle")

    return render(request, "customer/payment_tracking.html", {"payments": payments})


def payment_view(request):
    return render(request, "customer/payment_successful.html")


def my_booking(request):
    user = request.user
    customer_data1 = customer.objects.get(customer_data=user)
    data = pay.objects.filter(book__customer=customer_data1)
    return render(request, "customer/my_orders.html", {"data": data})

def invoice_view(request, id):
    try:
        invoice = pay.objects.get(id=id, book__customer__customer_data=request.user)
    except pay.DoesNotExist:
        return redirect("my_orders")  # Or show an error message page

    return render(request, "customer/invoice.html", {"invoice": invoice})