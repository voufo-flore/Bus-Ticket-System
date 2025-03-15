from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, TicketForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Tickets, Agency, Bus
from django.contrib import messages

from django.contrib.auth.models import User, AbstractUser
from django.db import IntegrityError
import random


# Create your views here.

def index(request):
    agencies=Agency.objects.all()
    buses=Bus.objects.all()
    
    context={
        'agencies':agencies,
        'buses':buses
    }
    
    return render(request, 'index.html', context)

def agency(req, pk):
    station=Agency.objects.get(id=pk)
    buses=station.bus_set.all()
    total=buses.count
    context={
        'station':station,
        'buses':buses,
        'total':total
        
    }
    
    return render(req, 'agency.html', context)

def create_user(req):
    if req.method == 'POST':
        username=req.POST.get('username')   
        email=req.POST.get('email')
        password1=req.POST.get('password1')
        password2=req.POST.get('password2')
       
        
        if password1==password2:
            if User.objects.filter(email=email,).exists():
                messages.error(req, 'Email already in use')
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                messages.success(req, 'welcome, Account created')
                user.save()
                login(req, user)
                return redirect('home')
            
        else:
            messages.error(req, 'Passwords do not match')
            return redirect('register')
        
    return render(req, 'signup.html')

def login_user(req):
    if req.user.is_authenticated:
        return redirect('home')
    
    if req.method == 'POST':
        try:
            username=req.POST.get('username')   
            password=req.POST.get('password')
            user=authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                messages.error(req, 'Login succesful')
                return redirect('home')
            else:
                
                messages.error(req, 'Invalid Creditails')
                return redirect('login')
        
            
        except Exception as e:
            messages.error(req, 'An error Occoured :' + str(e))
    
    return render(req, 'signin.html')
        
    
def logout_user(req):
    logout(req)
    return redirect('home')

@login_required(login_url='register')
def book_ticket(req, pk):
    bus=Bus.objects.get(id=pk)
    seats=Tickets.objects.filter(bus=bus, paid=True).order_by('seat_number')
    print(seats)
    if req.method == "POST":
            ticktet_holder_first_name=req.POST.get('first-name')
            ticktet_holder_last_name=req.POST.get('last-name')
            phone=int(req.POST.get('phone'))
            email=req.POST.get('email')
            seat_number=int(req.POST.get('seat_number'))
            paid_with=req.POST.get('paid-with')
        
            try:
                i=random.randint(1, 9999999999)
                    
                ticket=Tickets(
                    ticktet_holder_first_name=ticktet_holder_first_name,
                    ticktet_holder_last_name=ticktet_holder_last_name,
                    phone=phone,
                    email=email,
                    seat_number=seat_number,
                    user=req.user,
                    bus=bus,
                    paid_with=paid_with,
                    ticket_number=i
                    
                    
                )
                if bus.sits_available>0:
                    bus.sits_available-=1
                    bus.save()
                    ticket.save()
                    
                    return redirect('payment', ticket.id)
                else:
                    return redirect('book_ticket', bus.id)
                
            except IntegrityError:
                messages.info(req, 'Seat Already Booked')
        
    context={
            
            'bus':bus,
            "seats":seats
            
            
        }
        
    return render(req, 'checkout.html', context)

def receipt(req):
    return render(req, 'receipt.html')

def transaction(req, pk):
    ticket=Tickets.objects.get(id=pk)
    i=str(random.randint(100000,999999))
    
    if req.method == 'POST':
        code=req.POST.get('code')
        
        
            
        if code == i:
            
                #message here
                ticket.payment_status='paid ✅'
                ticket.paid=True
                
                ticket.save()
                return redirect('receipt')
        else:
                ticket.payment_status='faliure to pay ticket'
                messages.error(req, 'Ticket Booked But not Piad, Please Pay Ticket')
                return redirect('book_ticket', pk=ticket.bus.id)
                
    context={
        'ticket':ticket,
        "i":i
    }
    return render(req, 'payment.html', context)
    

@login_required(login_url='register')
def ticket_details(req, pk):
    ticket=Tickets.objects.get(id=pk)
    return render(req, 'ticket_details.html')
    

#New views

def Bus_page(req):
    buses=Bus.objects.all()
    context={
        'buses':buses
    }
    return render(req, 'tickets.html', context)

def dashboard(req):
    return render(req, 'dasboard.html')
          
   
            
            