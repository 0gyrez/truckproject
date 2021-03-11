from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Truck_card
from .forms import TruckForm, PhotoForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def main_page(request):

    return redirect('main')

def get_trucks(request):
    form = TruckForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
                new_truck = Truck_card(
                    photo=form.photo,
                    truck_name=form.data["truck_name"],
                    truck_year=form.data["truck_year"],
                    mileage_in_km=form.data["mileage_in_km"],
                    location=form.data["location"],
                    price=form.data["price"],
                    HP=form.data["HP"],
                    torque=form.data["torque"],
                    weight=form.data["weight"],
                    max_speed=form.data["max_speed"],
                    fuel_tank=form.data["fuel_tank"],
                    lifting_capacity=form.data["lifting_capacity"],
                    description=form.data["description"]

                )
                new_truck.save()
    trucks = Truck_card.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        trucks = Truck_card.objects.filter(truck_name__icontains=search_query)
    else:
        trucks = Truck_card.objects.all()
    p = Paginator(trucks, 9)
    page_number = request.GET.get('page', 1)
    form = TruckForm()
    context = {
        "trucks": p.page(page_number),
        "form": form
    }

    return render(request, "main.html", context=context)

def photo_album(request, truck_id):
    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            if 'photo_album' in request.FILES:
                photo_form.photo = request.FILES['photo']
                photo_form.save()
    return redirect('request', 'main', truck_id=truck_id)

@login_required
def get_truck(request, truck_id):
    truck = Truck_card.objects.get(pk=truck_id)
    context = {
        'truck' : truck
    }
    return render(request, "truck.html", context=context)


def register(request):
    if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          new_user = form.save(commit=False)
          new_user.set_password(form.cleaned_data['password1'])
          new_user.save()
          return redirect('main')
    else:
      form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

def login_v(request):
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
           cd = form.changed_data
           user = authenticate(username=cd['username'], password=cd['password'])
           if user is not None:
               if user.is_active:
                   login(request, user)
                   return HttpResponse('Authenticated successfully')
               else:
                   return HttpResponse('Disabled account')
           else:
               return HttpResponse('Invalid login')
       return redirect('main')
    else:
        form=LoginForm()
    return render(request, 'login.html', {'form': form})

