from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from . import forms, models, serializers


class InstitutionViewSet(viewsets.ModelViewSet):
  queryset = models.Institution.objects.all()
  serializer_class = serializers.InstitutionSerializer

class StudentViewSet(viewsets.ModelViewSet):
  queryset = models.Student.objects.all()
  serializer_class = serializers.StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
  queryset = models.Course.objects.all()
  serializer_class = serializers.CourseSerializer

class DashboardView(generic.TemplateView):
  template_name = 'dashboard.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    institutions = models.Institution.objects.all()
    students = models.Student.objects.all()
    courses = models.Course.objects.all()
    context['institutions'] = institutions
    context['students'] = students
    context['courses'] = courses
    return context

def institution_list(request):
  institutions_list = models.Institution.objects.order_by('-id')
  paginator = Paginator(institutions_list, 7)
  page = request.GET.get('page')
  institutions = paginator.get_page(page)
  name_contains_query = request.GET.get('name_contains')
  if name_contains_query != '' and name_contains_query is not None:
    institutions = institutions.filter(name__icontains=name_contains_query)
  context = {
    'institutions_list': institutions_list,
    'institutions': institutions
  }
  return render(request, 'institutions.html', context)

class StudentListView(generic.ListView):
  model = models.Student
  paginate_by = 8
  context_object_name = 'students'
  template_name = 'students.html'

class CourseListView(generic.ListView):
  model = models.Course
  paginate_by = 8
  context_object_name = 'courses'
  template_name = 'courses.html'

class InstitutionCreateView(SuccessMessageMixin, generic.CreateView):
  model = models.Institution
  form_class = forms.InstitutionForm
  template_name = 'core/institution-form.html'
  success_url = reverse_lazy('institutions')
  success_message = "Institution created successfully."


class InstitutionUpdateView(SuccessMessageMixin, generic.UpdateView):
  model = models.Institution
  fields = '__all__'
  template_name = 'core/institution-update.html'
  success_url = reverse_lazy('institutions')
  success_message = "Institution updated successfully."

class InstitutionDeleteView(generic.DeleteView):
  model = models.Institution
  template_name = 'core/institution_confirm_delete.html'
  success_url = reverse_lazy('institutions')
