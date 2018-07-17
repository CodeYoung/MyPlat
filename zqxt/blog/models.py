#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Date		: 2018-7-6  14：38：00
# @Author	: Young	Li (237572892@qq.com)
# @Link		: http://www.YoungLynn.top
# @Version	: 0.0.1

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .fields import CompressedTextField, ListField

# Create your models here.

@python_2_unicode_compatible
class Author(models.Model):
	name=models.CharField(max_length=50)
	qq=models.CharField(max_length=10)
	addr=models.TextField()
	email=models.EmailField()

	def __str__(self):
		return self.name
	"""docstring for A"""
	#def __init__(self, arg):
	#	super(A, self).__init__()
	#	self.arg = arg

		
@python_2_unicode_compatible
class Article(models.Model):
	title=models.CharField(max_length=50)
	author=models.ForeignKey(Author,on_delete=True)
	#content=models.TextField()
	score=models.IntegerField()
	tags=models.ManyToManyField('Tag')
	labels=ListField()
	content=CompressedTextField(null=True,default='')
	#labels = ListField()
    #content = CompressedTextField(null=True, default='')

	def __str__(self):
		if self.title:
			return self.title
		else:
			return 'Young'
	"""docstring for Article"""
	#def __init__(self, arg):
	#	super(Article, self).__init__()
	#	self.arg = arg


@python_2_unicode_compatible
class Tag(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self):
		return self.name
	"""docstring for Tag"""
	#def __init__(self, arg):
	#	super(Tag, self).__init__()
	#	self.arg = arg
	name=models.CharField(max_length=50)

	def __str__(self):
		return self.name

