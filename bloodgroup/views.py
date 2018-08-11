# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Organization, BloodBank, BloodGroup, City
from django.core.paginator import Paginator
from .forms import SignupForm
def signupview(request):
	form=SignupForm()
	msg=""
	if request.method=="POST":
		user_profile = SignupForm(request.POST)
		if user_profile.is_valid():
			user_profile.save()
			msg="user created successfully!!"
		else:
			msg=user_profile._errors

	return render(request,"signup.html",{"form":form,
		"msg":msg})

def organizationsview(request):
	data= Organization.objects.all()
	return render(request, "organizations.html",{"objects":data})
def bloodbanksview(request):

	#data= BloodBank.objects.all()
	blood_banks={}
	group_name = ""
	pages = ""
	if request.method=="POST":
		data = request.POST
		group_name = data.get("bloodgroup")
		city_name = data.get("city")
		#import pdb; pdb.set_trace()
		page_num=data.get("page_num",1)
		if not page_num:
			page_num=1

		if city_name:
			req_city = City.objects.filter(name=city_name)
			if req_city:
				req_city =req_city[0]
			else:
				all_cities =  map(lambda x:x.name, City.objects.all())
				return render(request, 
					"bloodbanks.html",
					{"city": city_name,
					"page_num": page_num,
					"group":group_name,
					"error":"Entered city not found valid city names:"+str(all_cities)}
					)
			blood_banks = BloodBank.objects.filter(
				bloodgroups__name=group_name,
				organization__city=req_city)

		pages = Paginator(blood_banks,100)

		return render(request, "bloodbanks.html",
			{ "objects":pages.page(page_num),
			"group":group_name,
			"page_num": page_num,
			"pages":pages,
			"city": city_name})
	return render(request, "bloodbanks.html")
def bloodgroupsview(request):
	data= BloodGroup.objects.all()
	return render(request, "bloodgroup.html",{"objects":data})


