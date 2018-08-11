# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Country)
admin.site.register(models.State)
admin.site.register(models.City)
admin.site.register(models.Organization)
admin.site.register(models.BloodGroup)
admin.site.register(models.BloodBank)
admin.site.register(models.UserProfile)
