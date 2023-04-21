from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home(request):

    return render(request,"home.html")

def register(request):    
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
       
        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff="True"
           
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('Register')        
    else:
        form=CreateUserForm()        
        return render(request,"register.html",{'form':form})
    
@login_required
def profile(request):
    return render(request,"profile.html")
    
def book(request):
    if request.method == 'POST':
        from_city = request.POST.get('from')
        to_city = request.POST.get('to')
        
        
        flights = Flight.objects.filter(
            orgin=from_city,
            destination=to_city,
           
        )
        
        context = {
            'flights': flights,
            'from_city':from_city,
            'to_city': to_city,
           
        }
        
        return render(request, 'bookk.html', context)
    
    return render(request, 'booking.html')
 


def book_flight(request):
    if request.method == 'POST':
        # Get the form data
        flight_number = request.POST['flight_number']
        departure_city = request.POST['departure_city']
        arrival_city = request.POST['arrival_city']
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']

        # Create a new Flight object with the form data
        new_flight = Flight(flight_number=flight_number, 
                            departure_city=departure_city, 
                            arrival_city=arrival_city, 
                            departure_time=departure_time, 
                            arrival_time=arrival_time)
        new_flight.save()
        # Get the search criteria from the form
        departure_city = request.POST['departure_city']
        arrival_city = request.POST['arrival_city']
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']

        # Search for flights in the database based on the search criteria
        flights = Flight.objects.filter(departure_city=departure_city, 
                                        arrival_city=arrival_city, 
                                        departure_time__gte=departure_time, 
                                        arrival_time__lte=arrival_time)

        # Render the search results page with the matching flights
        return render(request, 'bookk.html', {'flights': flights})
      

    else:
        # Render the flight booking page
        return render(request, 'booking.html')


def search_flights(request):
    if request.method == 'POST':
        # Get the search criteria from the form
        departure_city = request.POST['departure_city']
        arrival_city = request.POST['arrival_city']
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']

        # Search for flights in the database based on the search criteria
        flights = Flight.objects.filter(departure_city=departure_city, 
                                        arrival_city=arrival_city, 
                                        departure_time__gte=departure_time, 
                                        arrival_time__lte=arrival_time)

        # Render the search results page with the matching flights
        return render(request, 'search_results.html', {'flights': flights})

    else:
        # Render the flight search page
        return render(request, 'search_flights.html')

