from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
	input_type = 'date'

class RegisterForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	datebirth = forms.DateField(widget = DateInput)
	email = forms.EmailField()

	class Meta:
		#widgets = {'datebirth' : DateInput()}
		model = User
		fields = ["first_name","last_name","datebirth","email","username","password1","password2"]


