# -*- coding: utf-8 -*-
from basemodel.models import Organization
from django.db.models import Q
from django.template import Context,loader
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
#from django.http import Http404

class organization(object):
	"""docstring for organization"""
	def __init__(self, arg):
		super(organization, self).__init__()
		self.arg = arg


	def search(keywords):
		organization_list=get_object_or_404(Organization,Name=keywords)#Organization.objects.get(Q(Name=keywords))
		tmpl=loader.get_template('organization/organization_list.html')
		cont=Context({'organizations':organization_list})
		return HttpResponse(tmpl.render(cont))
