from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

class DateInput(forms.DateInput):
	input_type = 'date'

class RegisterForm(UserCreationForm):
	first_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
	datebirth = forms.DateField(widget = DateInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(
		widget = forms.TextInput(attrs={
			'class': 'form-control'
			}),
			error_messages = {'invalid': 'Type a valid format!'}
		)
	password1 = forms.CharField(
		label='Password',required=True, 
		widget=forms.PasswordInput(attrs={
			'class': 'form-control'
			}),
			error_messages = {'invalid': 'Check for typos!'}
		)
	password2 = forms.CharField(label='Password Verification',required=True,
		widget=forms.PasswordInput(attrs={
			'class': 'form-control'
			}),
			error_messages = {'invalid': 'Check for typos!'}
		)



	class Meta:
		
		model = User
		fields = ["first_name","last_name","datebirth","email","username","password1","password2"]
		widgets = {
		'first_name':forms.TextInput(attrs={'class': 'form-control'}),
		'last_name':forms.TextInput(attrs={'class': 'form-control'}),
		'email':forms.TextInput(attrs={'class': 'form-control'}),
		'username':forms.TextInput(attrs={'class': 'form-control'}),
		}

