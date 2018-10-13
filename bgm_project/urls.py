from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from bloodgroup.views import signupview, organizationsview,\
bloodbanksview, bloodgroupsview, signinview, manageview, signoutview,\
homeview, DonarDetailView, DonarUpdateView, userorgview,org_create, org_update,\
create_blood_bank, bank_update, bank_delete


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
    url(r'^donar/(?P<pk>[0-9]+)/$', DonarDetailView.as_view()),
    url(r'^donar_update/(?P<pk>[0-9]+)/$', DonarUpdateView.as_view()),
    url(r'^userorgs/$', userorgview),
    url(r'^org_create/$', org_create),
    url(r'^org_update/(?P<pk>[0-9]+)/$', org_update),
    url(r'^bloodbank_create/$', create_blood_bank),
    url(r'^bank_update/(?P<pk>[0-9]+)/$', bank_update), 
    url(r'^bank_delete/(?P<pk>[0-9]+)/$', bank_delete),    
]
