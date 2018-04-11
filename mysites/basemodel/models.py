# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#医生
class Doctors(models.Model):
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
	Sex=models.CharField(max_length=10)
	Organization=models.ForeignKey('Organization',on_delete=True)
	Dept=models.ForeignKey('Dept',on_delete=True)
	FingerPrint=models.CharField(max_length=1000,null=True)
	PassWord=models.CharField(max_length=18)
	CreateTime=models.DateTimeField()
	LastLogTime=models.DateTimeField()
	IsForbidden=models.BooleanField()
	Remark=models.CharField(max_length=1000,null=True)

#机构（医院）
class Organization(models.Model):
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=20)
	Name=models.CharField(max_length=20)
	Phone=models.CharField(max_length=11,null=True)
	ManagersID=models.CharField(max_length=100)
	Address=models.CharField(max_length=500,null=True)
	CreateTime=models.DateTimeField()
	ModifyTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for Organization"""
	#def __init__(self, arg):
	#	super(Organization, self).__init__()
	#	self.arg = arg
		

#科室
class Dept(models.Model):
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=20)
	Name=models.CharField(max_length=20)
	Phone=models.CharField(max_length=11,null=True)
	ManagersID=models.CharField(max_length=100)
	Address=models.CharField(max_length=500,null=True)
	CreateTime=models.DateTimeField()
	ModifyTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for Dept"""
	#def __init__(self, arg):
	#	super(Dept, self).__init__()
	#	self.arg = arg
		

#客户（病人）
class Clients(models.Model):
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=20)
	Name=models.CharField(max_length=20)
	IDCard=models.CharField(max_length=20)
	YBCard=models.CharField(max_length=20)
	Phone=models.CharField(max_length=11,null=True)
	Email=models.CharField(max_length=100,null=True)
	WeChat=models.CharField(max_length=100,null=True)
	Age=models.IntegerField()
	Sex=models.CharField(max_length=10)
	FingerPrint=models.CharField(max_length=1000,null=True)
	PassWord=models.CharField(max_length=18)
	Cipher=models.CharField(max_length=6)
	CreateTime=models.DateTimeField()
	LastLogTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for Clients"""
	#def __init__(self, arg):
	#	super(Clients, self).__init__()
	#	self.arg = arg

#地址管理		
class Address(models.Model):
	ID=models.IntegerField(primary_key=True)
	ClientID=models.IntegerField()
	Address=models.CharField(max_length=500,null=True)
	Phone=models.CharField(max_length=11,null=True)
	Contacts=models.CharField(max_length=500)
	CreateTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for Address"""
	#def __init__(self, arg):
	#	super(Address, self).__init__()
	#	self.arg = arg


#药房
class DrugStore(models.Model):
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=20)
	Name=models.CharField(max_length=20)
	Phone=models.CharField(max_length=11,null=True)
	ManagersID=models.CharField(max_length=100)
	Address=models.CharField(max_length=500,null=True)
	CreateTime=models.DateTimeField()
	ModifyTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for DrugStore"""
	#def __init__(self, arg):
	#	super(DrugStore, self).__init__()
	#	self.arg = arg
		
		
class Medi(models.Model):
	ID=models.IntegerField(primary_key=True)
	Code=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	Spec=models.CharField(max_length=2000)
	ProducerID=models.IntegerField()
	GuidePrice=models.DecimalField(max_digits=2,decimal_places=2)
	DoseUnit=models.CharField(max_length=20)
	DoseFactor=models.IntegerField()
	OtpaUnit=models.CharField(max_length=20)
	OtpaPack=models.IntegerField()
	InpaUnit=models.CharField(max_length=20)
	InpaPack=models.IntegerField()
	HouseUnit=models.CharField(max_length=20)
	HousePack=models.IntegerField()
	Instructions=models.BinaryField()
	CreateTime=models.DateTimeField()
	ModifyTime=models.DateTimeField()
	Remark=models.CharField(max_length=1000,null=True)
	"""docstring for Medi"""
	#def __init__(self, arg):
	#	super(Medi, self).__init__()
	#	self.arg = arg
		