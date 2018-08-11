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

class State(NameAbstractModel):
	country = models.ForeignKey(Country)

	class Meta:
		db_table="state"

class City(NameAbstractModel):
	pincode = models.IntegerField()
	state = models.ForeignKey(State)

	class Meta:
		db_table = "city"

class Organization(models.Model):
	name = models.CharField(max_length=250)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State)
	city = models.ForeignKey(City)

class BloodGroup(models.Model):
	bloodgroups = [("ap","A+ve"),
	("an","A-ve"),
	("abn","AB-ve"),
	("abp","AB+ve"),
	("op","o+ve"),
	("on","o-ve"),
	("bp","B+ve"),
	("bn","B-ve")
	]
	name  = models.CharField(max_length=3, choices=bloodgroups)

	def __str__(self):
		#import pdb; pdb.set_trace()
		return self.get_name_display()

class BloodBank(models.Model):
	name= models.CharField(max_length=250)
	organization = models.ForeignKey(Organization)
	bloodgroups = models.ManyToManyField(BloodGroup)

	class Meta:
		db_table="bloodbank"


class UserProfile(User):
	
	bloodgroup = models.ForeignKey(BloodGroup)
	country = models.ForeignKey(Country)
	state = models.ForeignKey(State)
	city = models.ForeignKey(City)

	class Meta:
		db_table="userprofile"








