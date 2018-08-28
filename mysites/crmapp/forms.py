# -*- coding: utf-8 -*-
from django import forms

from .models import *
from users.models import User


class ClientForm(forms.ModelForm):
	"""docstring for AddClient"""
	def __init__(self, *arg,**kwargs):
		super(ClientForm, self).__init__(*arg,**kwargs)
		for field_name in self.base_fields:
			field=self.base_fields[field_name]
			field.widget.attrs.update({"class":"form-control"})
		#self.arg = arg
	#CompanyName=forms.CharField(label='所属公司：')
	#Owner=forms.ChoiceField(choices=User,label='所有者：')
	#Code=forms.CharField(label='编码',required=False)
	ProjectProcess=forms.CharField(label='项目进程',widget=forms.Textarea,required=False)
	FollowRecord=forms.CharField(label='跟进记录',widget=forms.Textarea,required=False)
	#Contacts=forms.ModelMultipleChoiceField(Contacts.objects.all())
	
	class Meta:
		"""docstring for Meta"""
		model=Client
		fields=['Code','CompanyName','Owner','Industry','IntentionalProducts','PurchasePoint','FollowRecord','Clients','ProjectProcess','Contacts','Address']


class ContactsForm(forms.ModelForm):
	"""docstring for AddContacts"""
	def __init__(self, *arg,**kwargs):
		super(ContactsForm, self).__init__(*arg,**kwargs)
		#self.Client=kwargs.pop('Client')
		for field_name in self.base_fields:
			field=self.base_fields[field_name]
			field.widget.attrs.update({"class":"form-control"})
		#self.arg = arg
	Name=forms.CharField(label='姓名：')
	#Owner=forms.ChoiceField(choices=User,label='所有者：')
	#ProjectProcess=forms.CharField(label='项目进程',widget=forms.Textarea,required=False)
	
	class Meta:
		"""docstring for Meta"""
		model=Contacts
		fields=['Name','Client','Role','Position','WeChat','QQ','Email','Contacts']
	
