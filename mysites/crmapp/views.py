from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from crmapp.models import Client

from .forms import *
# Create your views here.

def index(request):
	if request.user.is_authenticated:
		#print('user is authenticated')
		return getuserclients(request)#render(request,'user_clients/user_clients.html')#redirect(reverse('user_clients'))
	return render(request,'base_crm.html')
	#return redirect('user_clients')

@csrf_protect
@never_cache
def getuserclients(request):	
	if request.user.is_authenticated:
		clients=Client.objects.filter(Owner=request.user)
		print('user is authenticated')
		print(clients)
		return render(request,'user_clients/user_clients.html',{'clients':clients})
	else:
		return render(request,'base_crm.html')


def adduserclient(request):
	if request.method=="POST":
		form=ClientForm(request.POST)
		client=Client()
		#companyname=client._meta.get_field('CompanyName')
		#print(type(companyname))
		if form.is_valid():
			#print(type(form.clean()))
			#print(form.clean())
			for item in form.clean():
				setattr(client,item,form.clean()[item])
				print(item)
			client.save()
			
			print(client.Address)
			print(client.CompanyName)	
				#print(form.clean()[item])
			#client=Client(request.POST)
			#client.save()
			return HttpResponseRedirect('/')
	else:
		form=ClientForm()
		return render(request,'user_clients/client_form.html',{'form':form})

def userclient(request):
	form=ClientForm()
	return render(request,'user_clients/client_form.html',{'form':form})