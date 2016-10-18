from django.conf.urls import url, include
from django.contrib import admin
from myschool.views import welcome

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myschool/', include('myschool.urls')),
    url(r'^$', welcome, name='welcome'),
]
