# -*- coding: utf-8 -*-
 
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
    	return organization.organization.search(request.GET['organization'])
    	#message = '你搜索的机构为: ' + request.GET['organization']

    return HttpResponse(message)