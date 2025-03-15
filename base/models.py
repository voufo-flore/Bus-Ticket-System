from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

    

class Agency(models.Model):
    name=models.CharField(max_length=50, blank=False)
    address=models.CharField(max_length=50, blank=False, null=False)
    phone=models.CharField(max_length=50, blank=False)
    
    
    
    def __str__(self):
        return self.name
    
    
class Bus(models.Model):
    is_full=models.BooleanField(default=False)
    agency=models.ForeignKey(Agency,  on_delete=models.CASCADE)
    sits=models.IntegerField(default=70)
    sits_available=models.IntegerField(default=70)
    time=models.IntegerField(default=0)
    bus_number=models.CharField( max_length=50)
    amount=models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    departure_city = models.CharField(blank=False ,max_length = 150)
    arrival_city = models.CharField(blank=False ,max_length = 150)
    
    
    
    def __str__(self):
        return self.agency.name
    
    
    class Meta():
        ordering=['-sits']   

    

class Tickets(models.Model):
    bus=models.ForeignKey(Bus, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ticktet_holder_first_name=models.CharField(blank=False, max_length=100)
    ticktet_holder_last_name=models.CharField(blank=False, max_length=100)
    seat_number=models.IntegerField()
    ticket_number=models.IntegerField(default=0)
    paid=models.BooleanField(default=False)
    payment_status=models.CharField(default='pending', max_length=50)
    phone=models.CharField(max_length=50, blank=False)
    email=models.EmailField(blank=False, max_length=254)
    paid_with=models.CharField(blank=False, max_length=50)
    
    
    def __str__(self):
        return self.bus.bus_number 
    
    class Meta:
        unique_together=('bus', 'seat_number')
    

    


