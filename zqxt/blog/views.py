# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Author,Article,Tag


# Create your views here.
# Django debug toolbar test
def index(request):
	obj = Article.objects.all()#.prefetch_related("publisher")
	# obj = Book.objects.all().select_related("publisher")
	#obj_dict=model_to_dict(obj)
	return render(request, 'index.html', {'obj': obj})