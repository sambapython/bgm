# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
class NameAbstractModel(models.Model):
	# abstract 
	name=models.CharField(max_length=250)

	class Meta:
		abstract=True

class Country(models.Model):
	name=models.CharField(max_length=250, unique=True)
	desc = models.TextField(blank=True)
	class Meta:
		db_table="country"
	def __str__(self):
		return self.name

class State(NameAbstractModel):
	country = models.ForeignKey(Country)

	class Meta:
		db_table="state"
	def __str__(self):
		return self.name

class City(NameAbstractModel):
	pincode = models.IntegerField()
	state = models.ForeignKey(State)

	class Meta:
		db_table = "city"
	def __str__(self):
		return self.name

class BloodGroup(models.Model):
	name  = models.CharField(max_length=10)

	def __str__(self):
		#import pdb; pdb.set_trace()
		return self.get_name_display()
	def __str__(self):
		return self.name




class UserProfile(User):
	roles = [
		("orgadmin","Organization"),
		("donar","Single User")]
	
	bloodgroup = models.ForeignKey(BloodGroup)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State)
	city = models.ForeignKey(City)
	status = models.BooleanField(default=True)
	role=models.CharField(max_length=25, default="donar",
		choices=roles)

	class Meta:
		db_table="userprofile"

class Organization(models.Model):
	name = models.CharField(max_length=250)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State)
	city = models.ForeignKey(City)
	user = models.OneToOneField(UserProfile, blank=True,null=True)
	def __str__(self):
		return self.name
class BloodBank(models.Model):
	name= models.CharField(max_length=250)
	organization = models.ForeignKey(Organization)
	bloodgroups = models.ManyToManyField(BloodGroup)

	class Meta:
		db_table="bloodbank"
	def __str__(self):
		return self.name








