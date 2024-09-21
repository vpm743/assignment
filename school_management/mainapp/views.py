# from django.shortcuts import render

# # Create your views here.
# # mainapp/views.py
# from django.shortcuts import render, redirect
# from django.views.generic import CreateView, UpdateView, DeleteView
# from .models import School, Student
# from .forms import SchoolForm, StudentForm
# from .forms import *
from .serializers import *

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import School, Student
from .forms import SchoolForm, StudentForm

def home(request):
    schools = School.objects.all()
    students = Student.objects.all()
    return render(request, 'school_management\mainapp\templates\home.html', {'schools': schools, 'students': students})

# class CreateSchoolView(CreateView):
#     model = School
#     form_class = SchoolForm
#     template_name = 'mainapp/create_school.html'
#     success_url = '/school/'

# class CreateStudentView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'mainapp/create_student.html'
#     success_url = '/school/'

# class UpdateSchoolView(UpdateView):
#     model = School
#     form_class = SchoolForm
#     template_name = 'mainapp/update_school.html'
#     success_url = '/school/'

# class UpdateStudentView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'mainapp/update_student.html'
#     success_url = '/school/'

# class DeleteSchoolView(DeleteView):
#     model = School
#     template_name = 'mainapp/delete_school.html'
#     success_url = '/school/'

# class DeleteStudentView(DeleteView):
#     model = Student
#     template_name = 'mainapp/delete_student.html'
#     success_url = '/school/'

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': True, 'message': 'Schools retrieved successfully', 'data': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        school = queryset.get(pk=pk)
        serializer = self.get_serializer(school)
        return Response({'status': True, 'message': 'School retrieved successfully', 'data': serializer.data})

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': True, 'message': 'Students retrieved successfully', 'data': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        student = queryset.get(pk=pk)
        serializer = self.get_serializer(student)
        return Response({'status': True, 'message': 'Student retrieved successfully', 'data': serializer.data})

class SchoolStudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, school_pk=None):
        school = School.objects.get(pk=school_pk)
        students = school.student_set.all()
        serializer = self.get_serializer(students, many=True)
        return Response({'status': True, 'message': 'Students retrieved successfully', 'data': serializer.data})



# mainapp/views.py
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import School, Student

# class SchoolAPI(APIView):
#     def get(self, request, pk):
#         school = School.objects.get(pk=pk)
#         serializer = SchoolSerializer(school)
#         return Response({'status': True, 'message': 'School retrieved successfully', 'data': serializer.data})

# class StudentAPI(APIView):
#     def get(self, request, pk):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(student)
#         return Response({'status': True, 'message': 'Student retrieved successfully', 'data': serializer.data})

# class SchoolStudentsAPI(APIView):
#     def get(self, request, pk):
#         school = School.objects.get(pk=pk)
#         students = school.student_set.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response({'status': True, 'message': 'Students retrieved successfully', 'data': serializer.data})
    
