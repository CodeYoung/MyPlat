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


	def search(self,keywords):
		organization_list=Organization.objects.filter(Name=keywords)
		tmpl=loader.get_template('organization/organization_list.html')
		return HttpResponse(tmpl.render({'organizations':organization_list}))

	#查询机构
	def searchOrganization(request):
		context          = {}
		context['hello'] = 'Hello World!'
		return render(request, 'organization/organization_search.html', context)
	

	#新增机构
	def addOrganization(request):
		context          = {}
		context['hello'] = 'Hello World!'
		return render(request, 'organization/organization_form.html', context)