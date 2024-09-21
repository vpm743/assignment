# mainapp/ajax_views.py
from django.http import JsonResponse
from .models import School, Student

def list_schools(request):
    schools = School.objects.all()
    data = []
    for school in schools:
        data.append({'id': school.pk, 'name': school.name})
    return JsonResponse({'data': data})

def list_students(request):
    students = Student.objects.all()
    data = []
    for student in students:
        data.append({'id': student.pk, 'name': student.name, 'enrollment': student.enrollment, 'school': student.school.name})
    return JsonResponse({'data': data})