from django.shortcuts import render
import datetime
from django.views.generic import ListView, DetailView
from myschool.models import Student, Class, Payment
from django.db.models import Sum, Count, Min, Max, Avg


def daytime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'myschool/time.html', context)


def home(request):
    context = {'name': "Mozart's Friends"}
    return render(request, 'myschool/home.html', context)


class StudentList(ListView):
    ''' show all students together with links '''
    model = Student


class ClassList(ListView):
    ''' show all classes in a list '''
    model = Class


class PaymentList(ListView):
    model = Payment


class StudentPaymentsList(ListView):
    ''' show a list of all payments ordered by students.'''
    template_name = "myschool\studentpayments_list.html"
    queryset = Student.objects.annotate(payment_sum=Sum('payment__amount'))
    queryset = queryset.annotate(payment_count=Count('payment__amount'))
    context_object_name = 'student_payment_list'


class StudentDetailView(DetailView):
    queryset = Student.objects.annotate(sum=Sum('payment__amount'))
    queryset = queryset.annotate(payment_count=Count('payment__amount'))


class ClassDetailView(DetailView):
    ''' show details of a specific class '''
    queryset = Class.objects.annotate(count_students=Count('students'))

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        c = context['class']
        context['num_students'] = c.students.count
        context['studentlist'] = c.students.all()
        return context


class PaymentDetailView(DetailView):
    model = Payment


class StudentClassesView(DetailView):
    ''' show all the classes of a specific student '''
    template_name = "myschool/studentclasses_detail.html"
    queryset = Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StudentClassesView, self).get_context_data(**kwargs)
        s = context['student']
        num_classes = s.class_set.count
        classlist = s.class_set.all()
        dict_class_students = {}
        for c in classlist:
            dict_class_students[c] = c.students.all()
        context['num_classes'] = num_classes
        context['classlist'] = classlist
        context['dict_class_students'] = dict_class_students
        return context


class StudentPaymentsView(DetailView):
    ''' show all the payments of a specific student '''
    template_name = "myschool/studentpayments_detail.html"
    queryset = Student.objects.annotate(sum_pm=Sum('payment__amount'))
    queryset = queryset.annotate(avg_pm=Avg('payment__amount'))
    queryset = queryset.annotate(max_pm=Max('payment__amount'))
    queryset = queryset.annotate(min_pm=Min('payment__amount'))

    def get_context_data(self, **kwargs):
        context = super(StudentPaymentsView, self).get_context_data(**kwargs)
        s = context['student']
        context['num_pm'] = s.payment_set.count
        paymentlist = s.payment_set.all()
        context['paymentlist'] = paymentlist
        return context
