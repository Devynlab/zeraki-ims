from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
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

class InstitutionListView(generic.ListView):
  model = models.Institution
  context_object_name = 'institutions'
  template_name = 'institutions.html'

class StudentListView(generic.ListView):
  model = models.Student
  context_object_name = 'students'
  template_name = 'students.html'

class CourseListView(generic.ListView):
  model = models.Course
  context_object_name = 'courses'
  template_name = 'courses.html'

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
    try:
      messages.success(self.request, self.success_message)
      return super(InstitutionDeleteView, self).delete(request, *args, **kwargs)
    except ProtectedError:
      messages.error(self.request, "Can't delete institution as it has been assigned a course.")
      return redirect('institutions')
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
    try:
      messages.success(self.request, self.success_message)
      return super(CourseDeleteView, self).delete(request, *args, **kwargs)
    except:
      messages.error(self.request, "Can't delete course as it has been assigned a student.")
      return redirect('courses')
