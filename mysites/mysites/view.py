# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def searchOrganization(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'organization/organization_search.html', context)
	

def addOrganization(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'organization/organization_form.html', context)