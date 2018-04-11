# -*- coding: utf-8 -*-
from basemodel.models import Organization
from django.db.models import Q
from django.template import Context,loader
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import organization
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    message = '你提交了空表单'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
        
    if 'organization' in request.GET:
    	#organization_list=get_object_or_404(Organization,Name=request.GET['organization'])
    	#organization_list=Organization.objects.all()#filter(Name=request.GET['organization'])
    	#tmpl=loader.get_template('organization/organization_list.html')
    	#cont=Context({'organizations':organization_list})
    	#return HttpResponse(tmpl.render({'organizations':organization_list}))
    	org=organization.organization(request.GET['organization'])
    	#return org.search('chongfuyi')
    	return org.search(request.GET['organization'])
    	#return organization.organization.search(request.GET['organization'])
    	#message = '你搜索的机构为: ' + request.GET['organization']

    return HttpResponse(message)