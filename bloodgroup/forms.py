from django import forms
from models import UserProfile
class SignupForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["username","email","password","bloodgroup",
		"country","state","city","role"]