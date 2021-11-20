from django.contrib import admin

from . import models

@admin.register(models.Institution)
class InstitutionAdmin(admin.ModelAdmin):
  list_display = ['name', 'website']

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'reg_num', 'institution', 'status']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['name', 'institution']
