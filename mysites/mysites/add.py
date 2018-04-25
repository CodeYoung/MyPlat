# -*- coding: utf-8 -*-
from basemodel.models import Organization
from django.db.models import Q
from django.template import Context,loader
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from basemodel import organization
import time
 
# 表单
def search_form(request):
	print(type(request))
	return render_to_response('search_form.html')
 
def add(request):
	print(type(request))
	request.encoding='utf-8'
	message = '你提交了空表单'
	message = '新增成功'
	if 'organizationcode' in request.GET:
		orgid=Organization.objects.latest('ID')
		org=Organization(ID=orgid.ID+1,Code=request.GET['organizationcode'],Name=request.GET['name'],Phone=request.GET['phone'],Address=request.GET['address'],CreateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),Remark=request.GET['remark'])
		org.save()
		return HttpResponse(message)