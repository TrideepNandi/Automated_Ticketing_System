from xml.dom.minidom import Attr
from django import forms
from trains.models import Station, TicketReservation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.contrib.auth import get_user_model

class TrainSearchForm(forms.Form):
    from_station = forms.ModelChoiceField(queryset=Station.objects.all(), label="From Station: ")
    to_station = forms.ModelChoiceField(queryset=Station.objects.all(), label="To Station: ")
    date_of_journey = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class' : 'date-input'}))
    
class BookSeatForm(forms.Form):
    passenger_name = forms.CharField(label='Passenger Name', max_length=30)
    passenger_age = forms.IntegerField(label='Passenger Age')
    passenger_sex = forms.ChoiceField(label='Passenger Sex', choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer Not to Say'),
    ))
    """class Meta:
        model = TicketReservation
        fields = ['passenger_name', 'passenger_age', 'passenger_sex']"""

class PNRStatusForm(forms.Form):
    pnr = forms.CharField(label='Enter your PNR number ', max_length=18, widget= forms.TextInput(attrs={'class': 'from_station1'}))

class CancelTicketForm(forms.Form):
    pnr = forms.CharField(label='PNR Number', max_length=18)
 
class RegistrationForm (UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1",)
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use. Please choose a different one.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("You already have an account associated with this email address")
        return email
