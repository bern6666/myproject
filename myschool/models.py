from django.db import models


class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    salutation = models.CharField(max_length=20)
    birthdate = models.DateField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name', 'birthdate')


class Class(models.Model):
    designation = models.CharField(max_length=30)
    teacher = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return '%s %s' % (self.designation, self.teacher)

    class Meta:
        ordering = ('designation',)
        verbose_name_plural = 'classes'


class Payment(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.ForeignKey('Student', on_delete=models.CASCADE,)

    def __str__(self):
        return '%s %s %s' % (self.date, self.amount, self.student)

    class Meta:
        ordering = ('date', 'student',)
