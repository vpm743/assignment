from django.contrib import admin

# Register your models here.
# mainapp/admin.py


# mainapp/admin.py
from django.contrib import admin
from .models import School, Student

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'enrollment', 'school', 'created_at', 'updated_at')
    search_fields = ('name', 'enrollment')

admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)