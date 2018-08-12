from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from bloodgroup.views import signupview, organizationsview,\
bloodbanksview, bloodgroupsview, signinview, manageview, signoutview,\
homeview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', homeview),
    url(r'^signup/', signupview),
    url(r'^organizations/', organizationsview),
    url(r'^bloodbanks/', bloodbanksview),
    url(r'^bloodgroups/', bloodgroupsview),
    url(r'^signin/', signinview),
    url(r'^signout/', signoutview),
    url(r'^manage/', manageview),

]
