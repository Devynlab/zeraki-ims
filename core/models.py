from django.db import models

class Institution(models.Model):
  INSTITUTION_TYPE_CHOICES = [
    ('university', 'University'),
    ('college', 'College'),
    ('tvet', 'TVET')
  ]
  name = models.CharField(max_length=70, unique=True)
  address = models.CharField(max_length=20)
  website = models.URLField()
  location = models.CharField(max_length=50)
  year_founded = models.PositiveIntegerField()
  institution_type = models.CharField(max_length=10, choices=INSTITUTION_TYPE_CHOICES)
  vision = models.TextField()

  def __str__(self) -> str:
    return self.name

class Student(models.Model):
  GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female')
  ]
  reg_num = models.CharField(max_length=17, unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, blank=True, null=True)
  course = models.ForeignKey('Course', on_delete=models.SET_NULL, blank=True, null=True)
  gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
  guardian = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  passport = models.ImageField(upload_to='media/passports')
  status = models.BooleanField(default=True)

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"

class Course(models.Model):
  name = models.CharField(max_length=50, unique=True)
  institution = models.ManyToManyField(Institution)
  units = models.ManyToManyField('Unit')

  def __str__(self) -> str:
    return self.name

class Unit(models.Model):
  unit_id = models.CharField(max_length=8, unique=True)
  name = models.CharField(max_length=50)

  def __str__(self) -> str:
    return f"{self.unit_id} - {self.name}"
