# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, redirect
from models import Organization, BloodBank, BloodGroup, City,\
UserProfile, State, Country
from django.core.paginator import Paginator
from .forms import SignupForm, OrganizationForm, BloodbankForm
from django.contrib.auth import authenticate
from django.views.generic import DetailView, UpdateView, CreateView
'''
class OrgCreateView(CreateView):
    model = Organization
    fields=("name","country","state","city")
    success_url="/userorgs/"

    def form_valid(self, form):
        form_dup = form.data.copy()
        up_id = self.request.session.get("user").get("id")
        up = UserProfile.objects.get(pk=up_id)
        form_dup.update({"user": up})
        form.data = form_dup
        import pdb; pdb.set_trace()
        response = super(OrgCreateView, self).form_valid(form)
        # do something with self.object
        return response
'''
def bank_update(request, pk):
    bloodbank = BloodBank.objects.get(pk=pk)
    form = BloodbankForm(instance=bloodbank)
    if request.method=="POST":
        form = BloodbankForm(instance=bloodbank, 
            data=request.POST)
        form.save()
        return redirect("/userorgs/")
    return render(request, "bloodgroup/bloodbank_form.html/",
        {"form": form})
def bank_delete(request, pk):
    bloodbank = BloodBank.objects.get(pk=pk)
    if request.method == "POST":
        bloodbank.delete()
        return redirect("/userorgs/")
    return render(request, "bloodgroup/bloodbank_delete.html")
def create_blood_bank(request):
    form = BloodbankForm()
    if request.method=="POST":
        data = request.POST
        user_id = request.session.get("user").get("id")
        org = Organization.objects.get(user__id=user_id)
        req_data={}
        req_data["name"]=data.get("name")
        req_data["organization"] = org
        bank = BloodBank(**req_data)
        bank.save()
        for group in data.get("bloodgroups"):
            inst = BloodGroup.objects.get(pk=group)
            bank.bloodgroups.add(inst)
        return redirect("/userorgs/")
    return render(request,"bloodgroup/bloodbank_form.html",
        {"form":form})

def org_update(request, pk):
    org = Organization.objects.get(pk=pk)
    if request.method=="POST":
        form = OrganizationForm(instance=org,data=request.POST)
        form.save()
        return redirect("/userorgs/")
    form = OrganizationForm(instance=org)
    return render(request,"bloodgroup/organization_form.html",{"form":form})

def org_create(request):
    form = OrganizationForm()
    if request.method=="POST":
        req_data={}
        data = request.POST
        user_id = request.session.get("user").get("id")
        up = UserProfile.objects.get(pk=user_id)
        req_data["state"] = State.objects.get(pk=data["state"])
        req_data["city"] = City.objects.get(pk=data["city"])
        req_data["country"] = Country.objects.get(pk=data["country"])
        req_data["user"]=up
        req_data["name"]=data.get("name")
        org = Organization(**req_data)
        org.save()
        return redirect("/userorgs/")
    return render(request,"bloodgroup/organization_form.html",
        {"form":form})
def userorgview(request):
    pk = request.session['user']['id']
    user_details=[]
    org_details=[]
    bloodbanks=[]
    try:
        user_details = UserProfile.objects.get(id=pk)
        org_details = Organization.objects.get(user__id=pk)
        bloodbanks = BloodBank.objects.filter(organization=org_details)
    except Exception as err:
        print err
    return render(request,"org_manage.html",
        {"user_details":user_details,
        "org_details":org_details,
        "bloodbanks":bloodbanks
        }
        )

class DonarDetailView(DetailView):
    model = UserProfile
class DonarUpdateView(UpdateView):
    model = UserProfile
    fields = ['bloodgroup','country','state','city','status']
    success_url="/manage/"
    #template_name=""

def homeview(request):
    return render(request,"base.html")
def signoutview(request):
    if request.method=="POST":
        request.session["user"]=None
        return redirect(homeview)
    return render(request,"signout.html")
def manageview(request):
    return render(request,"manage.html")

def signinview(request):
    msg=""
    request.session["user"] = None
    if request.method=="POST":
        data = request.POST
        user = authenticate(username=data.get("username"),
            password=data.get("password"))
        if user:
            user_profiles = UserProfile.objects.filter(user_ptr=user)
            if user_profiles:
                user_profile = user_profiles[0]

                request.session["user"]={"username":user.username,
                "role":user_profile.role,"id":user_profile.id}
                msg="login success"
                return redirect(manageview)
            else:
                msg="User profile not found for this user"
        else:
            msg="login failed"
    return render(request,"signin.html",{"msg":msg})

def signupview(request):
    form=SignupForm()
    msg=""
    if request.method=="POST":
        user_profile = SignupForm(request.POST)
        if user_profile.is_valid():
            UserProfile.objects.create_user(**user_profile.cleaned_data)
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


