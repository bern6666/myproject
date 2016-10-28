from django.conf.urls import url
from . import views
from myschool.views import StudentList, ClassList, PaymentList,\
    StudentPaymentsList, StudentPaymentsView, StudentDetailView,\
    StudentClassesView, ClassDetailView, PaymentDetailView

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # simple List View
    # all students with links to payments and classes
    url(r'^students/$', StudentList.as_view(), name='students'),
    # all classes with number of students
    url(r'^classes/$', ClassList.as_view(), name='classes'),
    # all payments ordered by date with Links
    url(r'^payments/$', PaymentList.as_view(), name='payments'),
    # all payments ordered by students
    url(r'^studentpayments/$', StudentPaymentsList.as_view(),
        name='studentpayments'),

    # Detail View of an individual student
    url(r'^student/(?P<pk>\d{1,2})/$', StudentDetailView.as_view(),
        name='student_detail'),

    # Detail View of an individual classs
    url(r'^class/(?P<pk>\d{1,2})/$', ClassDetailView.as_view(),
        name='class_detail'),

    # Detail View of an individual payment
    url(r'^payment/(?P<pk>\d{1,2})/$', PaymentDetailView.as_view(),
        name='payment_detail'),

    # Detail View for an individual student all classes
    url(r'^studentclasses/(?P<pk>\d{1,2})/$', StudentClassesView.as_view(),
        name='studentclasses_detail'),
    # Detail View for an individual student all payments
    url(r'^studentpayments/(?P<pk>\d{1,2})/$', StudentPaymentsView.as_view(),
        name='studentpayments_detail'),

]
