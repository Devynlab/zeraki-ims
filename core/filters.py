import django_filters

from core import models

class InstitutionFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(lookup_expr='icontains')

  class Meta:
    model = models.Institution
    fields = ['name']
