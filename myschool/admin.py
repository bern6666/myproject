from django.contrib import admin
from .models import Student, Class, Payment


class ClassAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)


admin.site.register(Student)
admin.site.register(Class, ClassAdmin)
admin.site.register(Payment)
