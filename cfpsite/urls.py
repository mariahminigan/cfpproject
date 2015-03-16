from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), #Directs /admin/ url to the view for the admin page. 
    url(r'',include('questionblog.urls')), #Redirects everything going into the main url to the questionblog.urls file.
]
