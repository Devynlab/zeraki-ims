from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
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
  name_contains_query = request.GET.get('name_contains')
  if name_contains_query != '' and name_contains_query is not None:
    institutions = institutions_list.filter(name__icontains=name_contains_query)
  paginator = Paginator(institutions_list, 7)
  page = request.GET.get('page')
  institutions = paginator.get_page(page)
  context = {
    'institutions_list': institutions_list,
    'institutions': institutions
  }
  return render(request, 'institutions.html', context)

def student_list(request):
  students_list = models.Student.objects.order_by('-id')
  paginator = Paginator(students_list, 10)
  page = request.GET.get('page')
  students = paginator.get_page(page)
  name_contains_query = request.GET.get('first_name_contains')
  if name_contains_query != '' and name_contains_query is not None:
    students = students.filter(name__icontains=name_contains_query)
  context = {
    'students_list': students_list,
    'students': students
  }
  return render(request, 'students.html', context)

def course_list(request):
  courses_list = models.Course.objects.order_by('-id')
  paginator = Paginator(courses_list, 7)
  page = request.GET.get('page')
  courses = paginator.get_page(page)
  name_contains_query = request.GET.get('name_contains')
  if name_contains_query != '' and name_contains_query is not None:
    courses = courses.filter(name__icontains=name_contains_query)
  context = {
    'courses_list': courses_list,
    'courses': courses
  }
  return render(request, 'courses.html', context)

class InstitutionCreateView(SuccessMessageMixin, generic.CreateView):
  model = models.Institution
  form_class = forms.InstitutionForm
  template_name = 'core/institution-form.html'
  success_url = reverse_lazy('institutions')
  success_message = "Institution created successfully."

class StudentCreateView(SuccessMessageMixin, generic.CreateView):
  model = models.Student
  form_class = forms.StudentForm
  template_name = 'core/student-form.html'
  success_url = reverse_lazy('students')
  success_message = "Student created successfully."

class CourseCreateView(SuccessMessageMixin, generic.CreateView):
  model = models.Course
  form_class = forms.CourseForm
  template_name = 'core/course-form.html'
  success_url = reverse_lazy('courses')
  success_message = "Course created successfully."

class InstitutionUpdateView(SuccessMessageMixin, generic.UpdateView):
  model = models.Institution
  form_class = forms.InstitutionForm
  template_name = 'core/institution-update.html'
  success_url = reverse_lazy('institutions')
  success_message = "Institution updated successfully."

class StudentUpdateView(SuccessMessageMixin, generic.UpdateView):
  model = models.Student
  form_class = forms.StudentForm
  template_name = 'core/student-update.html'
  success_url = reverse_lazy('students')
  success_message = "Student updated successfully."

class CourseUpdateView(SuccessMessageMixin, generic.UpdateView):
  model = models.Course
  form_class = forms.CourseForm
  template_name = 'core/course-update.html'
  success_url = reverse_lazy('courses')
  success_message = "Course updated successfully."

class InstitutionDeleteView(SuccessMessageMixin, generic.DeleteView):
  model = models.Institution
  template_name = 'core/institution_confirm_delete.html'
  success_url = reverse_lazy('institutions')
  success_message = "Institution deleted successfully."

  def delete(self, request, *args, **kwargs):
    if ProtectedError:
      messages.error(self.request, "Can't delete institution as it has been assigned a course.")
      return redirect('institutions')
    messages.success(self.request, self.success_message)
    return super(InstitutionDeleteView, self).delete(request, *args, **kwargs)

class StudentDeleteView(generic.DeleteView):
  model = models.Student
  template_name = 'core/student_confirm_delete.html'
  success_url = reverse_lazy('students')
  success_message = "Student deleted successfully."

class CourseDeleteView(generic.DeleteView):
  model = models.Course
  template_name = 'core/course_confirm_delete.html'
  success_url = reverse_lazy('courses')
  success_message = "Course deleted successfully."

  def delete(self, request, *args, **kwargs):
    if ProtectedError:
      messages.error(self.request, "Can't delete course as it has been assigned a student.")
      return redirect('courses')
    messages.success(self.request, self.success_message)
    return super(CourseDeleteView, self).delete(request, *args, **kwargs)

