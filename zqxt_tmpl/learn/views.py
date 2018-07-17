from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  home(request):
	List=map(str,range(100))
	return render(request,'home.html',{'List':List})
	#info_dict={'site':u'YOUNG学堂','content':u'各种IT技术教程'}
	#return render(request,'home.html',{'info_dict':info_dict})
	#TutorialList=["HTML","CSS","jQuery","Python","Django"]
	#return render(request,'home.html',{'TutorialList':TutorialList})
	#string=u"我在YOUNG学堂学习Django,用它来建网站"
	#return render(request,'home.html',{'string':string})

def add(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))