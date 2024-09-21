# # mainapp/urls.py
# from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('create_school/', views.CreateSchoolView.as_view(), name='create_school'),
#     path('create_student/', views.CreateStudentView.as_view(), name='create_student'),
#     path('update_school/<pk>/', views.UpdateSchoolView.as_view(), name='update_school'),
#     path('update_student/<pk>/', views.UpdateStudentView.as_view(), name='update_student'),
#     path('delete_school/<pk>/', views.DeleteSchoolView.as_view(), name='delete_school'),
#     path('delete_student/<pk>/', views.DeleteStudentView.as_view(), name='delete_student'),
# ]
# # mainapp/urls.py
# from django.urls import path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'schools', views.SchoolAPI, basename='schools')
# router.register(r'students', views.StudentAPI, basename='students')
# router.register(r'schools/(?P<pk>\d+)/students', views.SchoolStudentsAPI, basename='school_students')

# from django.urls import include, path

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# # mainapp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('schools/', views.school_list, name='school_list'),
#     path('schools/<int:pk>/', views.school_detail, name='school_detail'),
#     path('students/', views.student_list, name='student_list'),
#     path('students/<int:pk>/', views.student_detail, name='student_detail'),
# ]

# from django.urls import path, include
# from rest_framework import routers
# from .views import SchoolViewSet, StudentViewSet, SchoolStudentsViewSet

# router = routers.DefaultRouter()
# router.register(r'schools', SchoolViewSet, basename='schools')
# router.register(r'students', StudentViewSet, basename='students')
# router.register(r'schools/(?P<school_pk>\d+)/students', SchoolStudentsViewSet, basename='school-students')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
# from django.urls import path
# from .views import SchoolAPI, StudentAPI, SchoolStudentsAPI

# urlpatterns = [
#     path('api/schools/<pk>/', SchoolAPI.as_view()),
#     path('api/students/<pk>/', StudentAPI.as_view()),
#     path('api/schools/<pk>/students/', SchoolStudentsAPI.as_view()),
# ]

from django.urls import path, include
from rest_framework import routers
from .views import SchoolViewSet, StudentViewSet, SchoolStudentsViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='schools')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'schools/(?P<school_pk>\d+)/students', SchoolStudentsViewSet, basename='school-students')

urlpatterns = [
    path('', views.home, name='home'),
    # path('create_school/', views.CreateSchoolView.as_view(), name='create_school'),
    # path('create_student/', views.CreateStudentView.as_view(), name='create_student'),
    # path('update_school/<pk>/', views.UpdateSchoolView.as_view(), name='update_school'),
    # path('update_student/<pk>/', views.UpdateStudentView.as_view(), name='update_student'),
    # path('delete_school/<pk>/', views.DeleteSchoolView.as_view(), name='delete_school'),
    # path('delete_student/<pk>/', views.DeleteStudentView.as_view(), name='delete_student'),
    path('api/', include(router.urls)),
]