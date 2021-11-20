from django import forms

from . import models

INSTITUTION_TYPE_CHOICES = [
  ('university', 'University'),
  ('college', 'College'),
  ('tvet', 'TVET')
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
