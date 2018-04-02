# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ClassName(models.Model):
	"""docstring for ClassName"""
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=20)
	Name=models.CharField(max_length=20)
	IDCard=models.CharField(max_length=20)
	Phone=models.CharField(max_length=11)
	Email=models.CharField(max_length=100,null=True)
	WeChat=models.CharField(max_length=100,null=True)
	Age=models.IntegerField()
	Sex=models.CharField(max_lengh=10)
	Organization=models.ForeignKey('Organization',null=True)
	Dept=models.ForeignKey('Dept',null=True)
	FingerPrint=models.CharField(max_length=1000,null=True)
	PassWord=models.CharField(max_length=18)
	CreateTime=models.DateTimeField()
	LastLogTime=models.DateTimeField()
	IsForbidden=models.BooleanField()
	Remark=models.CharField(max_lengh=1000,null=True)
