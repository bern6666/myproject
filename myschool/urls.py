from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.daytime, name='daytime'),
    url(r'^students/$', views.students, name='students'),
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^payments/$', views.payments, name='payments'),
]
