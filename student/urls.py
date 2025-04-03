"""
URL configuration for student project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', BASE, name='base'),
    path('Dashboard', DASHBOARD, name='dashboard'),
    path('', LOGIN, name='login'),
    path('doLogin', doLogin, name='doLogin'),
    path('doLogout', doLogout, name='logout'),

    #profile path
    path('Profile', PROFILE, name='profile'),
    path('Profile/update', PROFILE_UPDATE, name='profile_update'),
    path('Password', CHANGE_PASSWORD, name='change_password'),
    path('AddCourses', ADD_COURSES, name='add_courses'),
    path('ManageCourses', MANAGE_COURSES, name='manage_courses'),
    path('DeleteCourses/<str:id>', DELETE_COURSES, name='delete_courses'),
    path('UpdateCourses/<str:id>', UPDATE_COURSES, name='update_courses'),
    path('UpdateCoursesDetails', UPDATE_COURSES_DETAILS, name='update_courses_details'),
    path('AddSubject', ADD_SUBJECT, name='add_subject'),
    path('ManageSubject', MANAGE_SUBJECT, name='manage_subject'),
    path('DeleteSubject/<str:id>', DELETE_SUBJECT, name='delete_subject'),
    path('RegisterStudents', REGISTER_STUDENTS, name='reg_students'),
    path('get_subjects/', get_subjects, name='get_subjects'),
    path('ManageStudents', MANAGE_STUDENTS, name='manage_students'),   
    path('DeleteStudents/<str:id>/', delete_Students, name='delete_Students'),
    path('UpdateStudent/<str:id>', UPDATE_STUDENTS, name='update_student'),
    path('UpdateStudentDetails', UPDATE_STUDENTS_DETAILS, name='update_student_details'),  
    path('data-between-dates/', data_between_dates, name='data_between_dates'),  
    path('search-students/', Search_Students, name='search-students'), 
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
