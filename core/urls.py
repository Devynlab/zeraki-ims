from django.urls import path

from . import views

urlpatterns = [
  path('', views.DashboardView.as_view(), name="dashboard"),
  path('institutions', views.InstitutionListView.as_view(), name="institutions"),
  path('students', views.StudentListView.as_view(), name="students"),
  path('courses', views.CourseListView.as_view(), name="courses"),
  path('units', views.UnitListView.as_view(), name="units")
]
