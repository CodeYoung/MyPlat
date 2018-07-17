# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render
from django.core.mail import send_mail
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def index(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'index.html', context)


def test(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'test.html', context)

def sendemail(request):
	context          = {}
	context['hello'] = 'Hello World!'
	send_mail('第一次邮件','这是第一次右键的内容',settings.DEFAULT_FROM_EMAIL,['1063991013@qq.com'],fail_silently=False)
	return render(request, 'index.html', context)
