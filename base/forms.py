from django.forms import ModelForm
`from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tickets
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta: 
        model=User
        fields= ('username','email','first_name', 'last_name' )
        labels={
            
            
        }
        help_texts={
            'username':'<br/>''enter user name here',
            
        }

class TicketForm(ModelForm):
    class Meta:
        model=Tickets
        fields=('ticktet_holder_first_name', 'ticktet_holder_last_name',)
        labels={
            'ticktet_holder_first_name':'First Name',
            'ticktet_holder_last_name':'Last Name'
        }
        widgets={
            'ticktet_holder_first_name':
                forms.TextInput(attrs={'class':'form'})
        }
        
