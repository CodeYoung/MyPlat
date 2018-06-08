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


def test(request):
	context          = {}
	context['hello'] = 'Hello World!'
	return render(request, 'test.html', context)

