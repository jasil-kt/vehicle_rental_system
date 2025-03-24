from django.shortcuts import render, redirect

from car_app.forms import vehicle_form
from car_app.models import owner, vehicle


def owner_dashboard(request):
    return render(request,'owner/owner_dashboard.html')

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

def vehicle_details(request):
    user = request.user
    owner_data = owner.objects.get(owner_data = user)
    data = vehicle.objects.filter(owner=owner_data)

    return render(request,"owner/view.html",{"data":data})

def update_vehicle(request,id):
    data = vehicle.objects.get(id=id)
    form1=vehicle_form(instance=data)
    if request.method == 'POST':
        data = vehicle_form(request.POST,instance=data)
        if data.is_valid():
            data.save()
        return redirect("vehicle_details")

    return render(request,"owner/edit_vehicle.html",{"owner_form":form1})

def delete_vehicle(request,id):
    data = vehicle.objects.get(id=id)
    data.delete()
    return redirect("vehicle_details")

    return render(request,"view.html")