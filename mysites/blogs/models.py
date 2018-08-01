# -*- coding: utf-8 -*-
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

class Article(models.Model):
	"""docstring for Article"""
	#def __init__(self, arg):
	#	super(Article, self).__init__()
	#	self.arg = arg
	title=models.CharField(u'标题',max_length=256)
	content=models.TextField(u'内容')

	pub_date=models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
	update_time=models.DateTimeField(u'更新时间',auto_now_add=True,null=True)

	def __str__(self):
		return self.title
		
