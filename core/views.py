from django.views import generic
from rest_framework import viewsets

from . import models, serializers


class InstitutionViewSet(viewsets.ModelViewSet):
  queryset = models.Institution.objects.all()
  serializer_class = serializers.InstitutionSerializer


class StudentViewSet(viewsets.ModelViewSet):
  queryset = models.Student.objects.all()
  serializer_class = serializers.StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
  queryset = models.Course.objects.all()
  serializer_class = serializers.CourseSerializer


class UnitViewSet(viewsets.ModelViewSet):
  queryset = models.Unit.objects.all()
  serializer_class = serializers.UnitSerializer


class DashboardView(generic.TemplateView):
  template_name = 'dashboard.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    institutions = models.Institution.objects.all()
    students = models.Student.objects.all()
    courses = models.Course.objects.all()
    units = models.Unit.objects.all()
    context['institutions'] = institutions
    context['students'] = students
    context['courses'] = courses
    context['units'] = units
    return context


class InstitutionListView(generic.ListView):
  model = models.Institution


class StudentListView(generic.ListView):
  model = models.Student


class CourseListView(generic.ListView):
  model = models.Course


class UnitListView(generic.ListView):
  model = models.Unit
