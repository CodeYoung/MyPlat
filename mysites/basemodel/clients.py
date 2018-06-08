# -*- coding: utf-8 -*-
from basemodel.models import Clients
from django.db.models import Q
from django.template import Context,loader
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404
import json
from django.core import serializers
#from django.http import Http404

#注册
def registerClient(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'client/client_register.html', context)
	

#登录
def loginClient(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'client/client_login.html', context)

def getClient(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'client/client_get.html', context)
