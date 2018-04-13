# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def index(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'index.html', context)

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