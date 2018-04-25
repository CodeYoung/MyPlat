# -*- coding: utf-8 -*-
from basemodel.models import Dept
from django.db.models import Q
from django.template import Context,loader
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
#from django.http import Http404

#查询部门
def searchDept(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'dept/dept_search.html', context)
	

#新增部门
def addDept(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'dept/dept_form.html', context)

class dept(object):
	"""docstring for organization"""
	def __init__(self, arg):
		super(dept, self).__init__()
		self.arg = arg


	def search(self,keywords):
		dept_list=Dept.objects.filter(Name=keywords)
		tmpl=loader.get_template('dept/dept_list.html')
		return HttpResponse(tmpl.render({'depts':dept_list}))
