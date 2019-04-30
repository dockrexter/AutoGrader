from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',include('home.urls')),
    url(r'^signup/',include('home.urls')),
    url(r'^login/',include('home.urls')),
    url(r'^assignment_upload',include('home.urls'))
    
]
