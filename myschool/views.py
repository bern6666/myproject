from django.shortcuts import render
import datetime
from django.views.generic import ListView, DetailView
from myschool.models import Student, Class, Payment
from django.db.models import Sum, Count, Min, Max, Avg
from django.http import HttpResponse


def daytime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'myschool/mytime.html', context)


def test(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'myschool/test_responsive.html', context)


def payments(request):
    context = {'now': datetime.datetime.now()}
    payment_list = Payment.objects.all()
    context['payment_list'] = payment_list
    q = Student.objects.annotate(payment_sum=Sum('payment__amount'))
    student_payment_list = q.annotate(payment_count=Count('payment__amount'))
    context['student_payment_list'] = student_payment_list
    return render(request, 'myschool/mypayments.html', context)


def search_ajax(request):
    if request.method == 'GET' and 'term' in request.GET:
        q = request.GET['term']
    else:
        q = ''
    studentlist = Student.objects.filter(last_name__startswith=q)
    # this looks for the first letters of the last name, independent of case
    # contains=q would look case sensitive,
    # whereas icontains=q looks case insensitive
    return render(request, 'myschool/myajax_snippet.html',
                  {'studentlist': studentlist, 'count': studentlist.count()})


# djangobook.com/django-forms
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            studentlist = Student.objects.filter(last_name__icontains=q)
            return render(request, 'myschool/mysearch.html',
                          {'studentlist': studentlist, 'query': q})
    return render(request, 'myschool/mysearch.html', {'error': error})


def home(request):
    context = {'name': "Mozart's Friends"}
    return render(request, 'myschool/myhome.html', context)


class StudentList(ListView):
    ''' show all students together with links '''
    model = Student  # short hand for the queryset= Student.objects.all()
    # default for templatename would be student_list.html
    template_name = "myschool/mystudent_list.html"


class ClassList(ListView):
    ''' show all classes in a list '''
    model = Class    # default would be class_list.html
    template_name = "myschool/myclass_list.html"


"""
class PaymentList(ListView):
    model = Payment


class StudentPaymentsList(ListView):
    ''' show a list of all payments ordered by students.'''
    template_name = "myschool\studentpayments_list.html"
    queryset = Student.objects.annotate(payment_sum=Sum('payment__amount'))
    queryset = queryset.annotate(payment_count=Count('payment__amount'))
    context_object_name = 'student_payment_list'

"""


class StudentDetailView(DetailView):
    queryset = Student.objects.annotate(sum=Sum('payment__amount'))
    queryset = queryset.annotate(payment_count=Count('payment__amount'))
    # default template name would be student_detail.html
    template_name = "myschool/mystudent_detail.html"


class ClassDetailView(DetailView):
    ''' show details of a specific class '''
    queryset = Class.objects.annotate(count_students=Count('students'))
    template_name = "myschool/myclass_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        c = context['class']
        context['num_students'] = c.students.count
        context['studentlist'] = c.students.all()
        return context


class PaymentDetailView(DetailView):
    model = Payment  # default template would be payment_detail.html
    template_name = "myschool/mypayment_detail.html"


class StudentClassesView(DetailView):
    ''' show all the classes of a specific student '''
    template_name = "myschool/mystudentclasses_detail.html"
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
    template_name = "myschool/mystudentpayments_detail.html"
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
