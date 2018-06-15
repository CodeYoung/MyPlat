from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for Blog"""
	#def __init__(self, arg):
	#	super(Blog, self).__init__()
	#	self.arg = arg
	name=models.CharField(max_length=50,default='default name')
	user_id=models.IntegerField(default=1)
	user_name=models.CharField(max_length=10,default='default name')
	content=models.CharField(max_length=500,default='default content')
	created_at=models.IntegerField(default=1514879938)

	def __str__(self):
		return self.name

class Comment(models.Model):
	"""docstring for Comment"""
	#def __init__(self, arg):
	#	super(Comment, self).__init__()
	#	self.arg = arg
	blog_id=models.IntegerField(default=1)
	user_id=models.IntegerField(default=1)
	user_name=models.CharField(max_length=10,default='default name')
	content=models.CharField(max_length=500,default='default content')	
	created_at=models.IntegerField(default=1514879938)

	def __str__(self):
		return self.user_name

