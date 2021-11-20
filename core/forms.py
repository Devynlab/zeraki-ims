from django import forms

from . import models

INSTITUTION_TYPE_CHOICES = [
  ('university', 'University'),
  ('college', 'College'),
  ('tvet', 'TVET')
]

GENDER_CHOICES = [
  ('male', 'Male'),
  ('female', 'Female')
]

class InstitutionForm(forms.ModelForm):
  class Meta:
    model = models.Institution
    fields = ['name', 'address', 'website', 'location', 'year_founded', 'institution_type', 'vision']
    widgets = {
      'name': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Name'
    }),
      'address': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Address'
    }),
      'website': forms.URLInput(attrs={
        'class': "form-control",
        'placeholder': 'Website'
    }),
      'location': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Location'
    }),
      'year_founded': forms.NumberInput(attrs={
        'class': "form-control",
        'placeholder': 'Year Founded'
    }),
      'institution_type': forms.Select(attrs={
        'class': "form-control",
        'placeholder': 'Institution Type'
    }),
      'vision': forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': 'Vision'
    })
  }

class StudentForm(forms.ModelForm):
  class Meta:
    model = models.Student
    fields = ['reg_num', 'first_name', 'last_name', 'email', 'institution', 'course', 'gender', 'guardian', 'date_of_birth', 'status']
    widgets = {
      'reg_num': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Registration Number'
    }),
      'first_name': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'First Name'
    }),
      'last_name': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Last Name'
    }),
      'email': forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Email'
    }),
      'institution': forms.Select(attrs={
        'class': "form-control"
    }),
      'course': forms.Select(attrs={
        'class': "form-control"
    }),
      'gender': forms.Select(attrs={
        'class': "form-control"
    }),
      'guardian': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Guardian'
    }),
      'date_of_birth': forms.DateInput(attrs={
        'class': "form-control",
        'placeholder': 'YYYY-MM-DD'
    }),
      'status': forms.CheckboxInput(attrs={
        'class': "form-control"
    })
  }

class CourseForm(forms.ModelForm):
  class Meta:
    model = models.Course
    fields = ['name', 'institution']
    widgets = {
      'name': forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Name'
    }),
      'institution': forms.Select(attrs={
        'class': "form-control",
        'placeholder': 'Institution'
      })
  }
