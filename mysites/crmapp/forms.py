from django import forms

from .models import *
from users.models import User


class ClientForm(forms.ModelForm):
	"""docstring for AddClient"""
	#def __init__(self, arg):
	#	super(AddClient, self).__init__()
	#	self.arg = arg
	#CompanyName=forms.CharField(label='所属公司：')
	#Owner=forms.ChoiceField(choices=User,label='所有者：')
	ProjectProcess=forms.CharField(label='项目进程',widget=forms.Textarea,required=False)
	class Meta:
		"""docstring for Meta"""
		model=Client
		fields=['CompanyName','Owner','Industry','IntentionalProducts','PurchasePoint','FollowRecord','Clients','ProjectProcess','Contacts','Address']

			
