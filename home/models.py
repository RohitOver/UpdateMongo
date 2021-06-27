from django.db import models

# Create your models here.

class Battery(models.Model):
	code = models.CharField(max_length=30)
	lower_limit = models.IntegerField()
	upper_limit = models.IntegerField()
	priority = models.IntegerField()
	class Meta:
		db_table = "battery1"	
