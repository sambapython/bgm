from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from bloodgroup.views import signupview, organizationsview


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', TemplateView.as_view(template_name="base.html")),
    url(r'^signup/', signupview),
    url(r'^organizations/', organizationsview),

]
