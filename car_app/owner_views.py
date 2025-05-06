from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from car_app.forms import vehicle_form
from car_app.models import owner, vehicle, book_now, pay


@login_required(login_url='landing')
def owner_dashboard(request):
    owner_obj = owner.objects.get(owner_data=request.user)
    total_vehicles = vehicle.objects.filter(owner=owner_obj).count()
    active_bookings = book_now.objects.filter(vehicle__owner=owner_obj, status=1).count()
    pending_payments = pay.objects.filter(book__vehicle__owner=owner_obj).count()

    return render(request, 'owner/owner_dashboard.html', {
        'total_vehicles': total_vehicles,
        'active_bookings': active_bookings,
        'pending_payments': pending_payments,
    })

@login_required(login_url='landing')
def add_vehicle(request):
    user_data = request.user
    owner_data = owner.objects.get(owner_data = user_data)
    if request.method == 'POST':
        form = vehicle_form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner= owner_data
            obj.save()
            return redirect("vehicle_details")
    else:
        form = vehicle_form()
    return render(request, 'owner/add_vehicle.html', {'form': form})

@login_required(login_url='landing')
def vehicle_details(request):
    user = request.user
    owner_data = owner.objects.get(owner_data = user)
    data = vehicle.objects.filter(owner=owner_data)

    return render(request,"owner/view.html",{"data":data})

@login_required(login_url='landing')
def update_vehicle(request,id):
    data = vehicle.objects.get(id=id)
    form1=vehicle_form(instance=data)
    if request.method == 'POST':
        data = vehicle_form(request.POST,instance=data)
        if data.is_valid():
            data.save()
        return redirect("vehicle_details")

    return render(request,"owner/edit_vehicle.html",{"owner_form":form1})

@login_required(login_url='landing')
def delete_vehicle(request,id):
    data = vehicle.objects.get(id=id)
    data.delete()
    return redirect("vehicle_details")

    return render(request,"view.html")

@login_required(login_url='landing')
def owner_booking_management(request):
    try:
        owner_data = owner.objects.get(owner_data=request.user)
    except owner.DoesNotExist:
        return redirect('owner_dashboard')


    owner_vehicles = vehicle.objects.filter(owner=owner_data)


    bookings = book_now.objects.filter(vehicle__in=owner_vehicles).order_by('-start_date')

    return render(request, "owner/booking_management.html", {
        "bookings": bookings,
        "owner": owner_data
    })