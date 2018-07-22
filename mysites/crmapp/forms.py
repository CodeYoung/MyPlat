from django import forms

from models import *


class AddClientForm(forms.ModelForm):
	"""docstring for AddClient"""
	#def __init__(self, arg):
	#	super(AddClient, self).__init__()
	#	self.arg = arg
	class Meta:
		"""docstring for Meta"""
		model=Client
		fields=['CompanyName']
			
