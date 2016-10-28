import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from myschool.models import Class, Student, Payment
from django.db.models import Avg, Sum, Max, Min, Count


def show_all_students_and_their_payments():
    studentlist = Student.objects.all()
    for s in studentlist:
        print(s)
        paylist = s.payment_set.all()
        count = paylist.count()

        aggreg = paylist.aggregate(Sum('amount'), Max('amount'), Min('amount'),
                                   Avg('amount'))
        avg = aggreg['amount__avg']
        sum = aggreg['amount__sum']
        max = aggreg['amount__max']
        min = aggreg['amount__min']
        print('count {} payments'.format(count))
        print('Sum: {0:5.2f}'.format(sum))
        print('Average: {0:5.2f}'.format(avg))
        print('Max: {0:5.2f}'.format(max))
        print('Min: {0:5.2f}'.format(min))
        for p in paylist:
            print(p.amount, p.date)
        print('----')
    show_menu()


def show_all_students_and_their_classes():
    studentlist = Student.objects.all()
    for s in studentlist:
        print(s)
        classlist = s.class_set.all()
        for c in classlist:
            print(c)
        print('----')
    show_menu()


def show_all_classes_and_their_students():
    classlist = Class.objects.all()
    for c in classlist:
        print(c)
        studentlist = c.students.all()
        for s in studentlist:
            print(s)
        print('----')
    show_menu()


def show_dict_of_all_classes_and_their_students():
    dict = {}
    classlist = Class.objects.all()
    for c in classlist:
        studentlist = c.students.all()
        dict[c] = studentlist
    for c, studentlist in dict.items():
        print(c)
        for s in studentlist:
            print(s)
        print('----')
    show_menu()


def show_all_students_and_sum_of_their_payments():
    queryset = Student.objects.annotate(sum=Sum('payment__amount'))
    queryset = queryset.annotate(count=Count('payment__amount'))
    print(queryset.query)
    for s in queryset:
        print("{0:>10} - sum:{1:8.2f} - number of payments{2:5d}".
              format(s.last_name, s.sum, s.count))
    show_menu()


def show_menu():
    print('1 - all students and their classes')
    print('2 - all classes and their students')
    print('3 - dict of all classes with their students')
    print('4 - all students and their payments')
    print('5 - all students and sum of their payments')
    print('0 - End')
    choice = input("Your choice? ")

    if (choice == '1'):
        show_all_students_and_their_classes()
    elif (choice == '2'):
        show_all_classes_and_their_students()
    elif (choice == '3'):
        show_dict_of_all_classes_and_their_students()
    elif (choice == '4'):
        show_all_students_and_their_payments()
    elif (choice == '5'):
        show_all_students_and_sum_of_their_payments()
    else:
        print('Fertig')
    return


# Start execution here!
if __name__ == "__main__":
    print("Starting MySchool Test script...")
    show_menu()
