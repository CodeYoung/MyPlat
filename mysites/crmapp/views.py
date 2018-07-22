from django.shortcuts import render,redirect

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from crmapp.models import Client
# Create your views here.

def index(request):
	return render(request,'user_clients.html')
	#return redirect('user_clients')

@csrf_protect
@never_cache
def getuserclients(request):	
	clients=Client.objects.filter(Owner=request.user)
	return render(request,'user_clients',{'clients':clients})


def adduserclient(request):
	client=Client()
	client.Owner=request.user
	client.CompanyName='我们公司'
	client.save()
	return redirect('user_clients')