from django.urls import path
# from django_filters.views import FilterView

from core import filters, models, views

urlpatterns = [
  path('', views.DashboardView.as_view(), name="dashboard"),
  path('institutions/', views.institution_list, name="institutions"),
  path('institution/add/', views.InstitutionCreateView.as_view(), name="add-institution"),
  path('institution/edit/<pk>/', views.InstitutionUpdateView.as_view(), name="edit-institution"),
  path('institution/delete/<pk>/', views.InstitutionDeleteView.as_view(), name="delete-institution"),
  path('students/', views.StudentListView.as_view(), name="students"),
  path('courses/', views.CourseListView.as_view(), name="courses")
]
