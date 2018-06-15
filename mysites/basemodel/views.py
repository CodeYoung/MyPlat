# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json
from users.models import User
from blogs.models import Blog

# Create your views here.
def index(request):
	a=Blog.objects.all().order_by('-id')[:5]
	return render(request,'basemain.html',{'blogs':a})


def accounts_profile(request):
	if request.method=='POST':
		a=json.loads(request.body)
		print(a)
		b=User.objects.get(email=request.user.email)
		b.Name=a['Name']
		b.save()
	return render(request,'accounts_profile.html')