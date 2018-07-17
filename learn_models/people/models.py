from django.db import models

# Create your models here.

class Person(models.Model):
	"""docstring for Person"""
	#def __init__(self, arg):
	#	super(Person, self).__init__()
	#	self.arg = arg
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	def __str__(self):
		return self.name

