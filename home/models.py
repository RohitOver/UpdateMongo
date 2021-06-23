from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)

class Battery(models.Model):
	code = models.CharField(max_length=30)
	lower_limit = models.CharField(max_length=30)
	upper_limit = models.CharField(max_length=30)
	priority = models.CharField(max_length=30)