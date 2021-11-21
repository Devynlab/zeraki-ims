from django.urls import path

from core import views

urlpatterns = [
  path('', views.DashboardView.as_view(), name="dashboard"),
  path('institutions/', views.InstitutionListView.as_view(), name="institutions"),
  path('students/', views.StudentListView.as_view(), name="students"),
  path('courses/', views.CourseListView.as_view(), name="courses"),
  path('institution/add/', views.InstitutionCreateView.as_view(), name="add-institution"),
  path('student/add/', views.StudentCreateView.as_view(), name="add-student"),
  path('course/add/', views.CourseCreateView.as_view(), name="add-course"),
  path('institution/edit/<pk>/', views.InstitutionUpdateView.as_view(), name="edit-institution"),
  path('student/edit/<pk>/', views.StudentUpdateView.as_view(), name="edit-student"),
  path('course/edit/<pk>/', views.CourseUpdateView.as_view(), name="edit-course"),
  path('institution/delete/<pk>/', views.InstitutionDeleteView.as_view(), name="delete-institution"),
  path('student/delete/<pk>/', views.StudentDeleteView.as_view(), name="delete-student"),
  path('course/delete/<pk>/', views.CourseDeleteView.as_view(), name="delete-course")
]
