from django import forms
from models import UserProfile, Organization, BloodBank
class SignupForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["username","email","password","bloodgroup",
		"country","state","city","role"]
class OrganizationForm(forms.ModelForm):
	class Meta:
		model=Organization
		exclude=["user"]
class BloodbankForm(forms.ModelForm):
	class Meta:
		model = BloodBank
		fields = ["name","bloodgroups"]