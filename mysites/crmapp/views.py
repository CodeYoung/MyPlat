# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
import json
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
		print(request.POST)
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

def searchUserClients(request):
	#if request.POST:
	clients=Client.objects.filter(Owner=request.user)
	returnData={"rows":[]} #########非常重要############
	for client in clients:
		print(client.CompanyName)
		if client.Owner is None:
			owner=""
		else:
			owner=client.Owner.Name
		if client.Clients is None:
			clientName=""
		else:
			clientName=client.Clients.CompanyName
		if client.Contacts is None:
			contacts=""
		else:
			contacts=client.Contacts.Name
		returnData['rows'].append({
			"id":client.id,
			"CompanyName":client.CompanyName,
			"Owner":owner,
			"Industry":client.Industry,
			"IntentionalProducts":client.IntentionalProducts,
			"PurchasePoint":client.PurchasePoint,
			"FollowRecord":client.FollowRecord,
			"Clients":clientName,
			"ProjectProcess":client.ProjectProcess,
			"Contacts":contacts,
			"Address":client.Address,
				})	
	#最后用dumps包装下
	return HttpResponse(json.dumps(returnData))#render(request,'user_clients/user_clients.html',{'clients':clients})

def editclient(request,client_id):
	client=Client.objects.get(pk=client_id)
	if request.method=='POST':
		print("POST")
		form=ClientForm(request.POST,instance=client)
		print(form)
		if form.is_valid():
			form.save()
			baseUrl="/"#"/".join(request.path.split("/")[:-2])
			print(baseUrl)
			return redirect(baseUrl)
	else:
		#print("get")
		form=ClientForm(instance=client)
		#print(form)
	return render(request,'user_clients/client_editform.html',{'form':form})
	
	#form=ClientForm()
	#return render(request,'user_clients/client_form.html',{'form':form})

def deleteclient(request,client_id):
	print(client_id)
	client=Client.objects.filter(pk=client_id).delete() #删除数据
	baseUrl="/"#"/".join(request.path.split("/")[:-2])
	print(baseUrl)
	return redirect(baseUrl)
	