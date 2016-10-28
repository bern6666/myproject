from django.conf.urls import url, include
from django.contrib import admin
from myschool.views import daytime

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myschool/', include('myschool.urls')),
    url(r'^$', daytime, name='daytime'),
]
