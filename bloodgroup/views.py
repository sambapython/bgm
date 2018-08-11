# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Organization, BloodBank, BloodGroup
def signupview(request):
	return render(request,"signup.html")

def organizationsview(request):
	data= Organization.objects.all()
	return render(request, "organizations.html",{"objects":data})
def bloodbanksview(request):
	data= BloodBank.objects.all()
	return render(request, "bloodbanks.html",{"objects":data})
def bloodgroupsview(request):
	data= BloodGroup.objects.all()
	return render(request, "bloodgroup.html",{"objects":data})


