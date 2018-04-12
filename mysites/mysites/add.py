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
 
def add(request):
    message = '新增操作'
    return HttpResponse(message)