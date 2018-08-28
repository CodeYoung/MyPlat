# -*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
import json
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from crmapp.models import Client

from .forms import *

import uuid
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
				if item=='Code':
					setattr(client,item,uuid.uuid1())
				else:
					setattr(client,item,form.clean()[item])
				#print(item)
			client.save()
			
			#print(client.Address)
			#print(client.CompanyName)	
				#print(form.clean()[item])
			#client=Client(request.POST)
			#client.save()
			return HttpResponseRedirect('/crmapp/editclient/'+str(client.id))
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

def editclient(request):

	
	if request.method=='POST':
		client_id=request.POST['clientId']
		client=Client.objects.get(pk=client_id)
		print("POST")
		form=ClientForm(request.POST,instance=client)
		print(form)
		if form.is_valid():
			form.save()
			baseUrl="/"#"/".join(request.path.split("/")[:-2])
			print(baseUrl)
			return redirect(baseUrl)
	else:
		client_id=request.GET['clientId']
		client=Client.objects.get(pk=client_id)
		#print("get")
		form=ClientForm(instance=client)
		#print(type(form))
		print(form)
	return render(request,'user_clients/client_editform.html',{'form':form})
	
	#form=ClientForm()
	#return render(request,'user_clients/client_form.html',{'form':form})

def deleteclient(request,client_id):
	print(client_id)
	client=Client.objects.filter(pk=client_id).delete() #删除数据
	baseUrl="/"#"/".join(request.path.split("/")[:-2])
	print(baseUrl)
	return redirect(baseUrl)
	

def managecontacts(request):
	
	if request.method=="POST":
		print(request.POST)
		client_id=request.POST['Client']
		#print(client_code)
		client=Client.objects.get(pk=client_id)
		if client:
			contactsList=Contacts.objects.filter(Client=client)
		else:
			print('对应的客户不存在')
			return HttpResponseRedirect('/')
		form=ContactsForm(request.POST)
		print(request.POST)
		contacts=Contacts()
		#companyname=client._meta.get_field('CompanyName')
		#print(type(companyname))
		if form.is_valid():
			#print(type(form.clean()))
			#print(form.clean())
			for item in form.clean():
				setattr(contacts,item,form.clean()[item])
				print(item)
			contacts.save()
			
			#print(client.Address)
			#print(client.CompanyName)	
				#print(form.clean()[item])
			#client=Client(request.POST)
			#client.save()
			return HttpResponseRedirect('/')
	else:
		return searchclientcontacts(request)


def searchclientcontacts(request):
	if request.method=="GET":

		client_id=request.GET['clientId']
	else:
		client_id=request.POST['clientId']
		#print(client_code)
	client=Client.objects.get(pk=client_id)
	if client:
		contactsList=Contacts.objects.filter(Client=client)
	else:
		print('对应的客户不存在')
		return HttpResponseRedirect('/')
	if contactsList==None or len(contactsList)==0:
		form=ContactsForm()
		print(form)
		return render(request,'client_contacts/contacts_form.html',{'form':form})
	else:
		returnData={"rows":[]} #########非常重要############
		for contact in contactsList:
			print(contact.Name)
			if contact.Contacts is None:
				contacts=""
			else:
				contacts=contact.Contacts.Name
			returnData['rows'].append({
				"id":contact.id,
				"Name":contact.Name,
				"Phone":contact.Phone,
				"Client":contact.Client.CompanyName,
				"Role":contact.Role,
				"Position":contact.Position,
				"WeChat":contact.WeChat,
				"QQ":contact.QQ,
				"Email":contact.Email,
				"Contacts":contacts,
					})	
		#最后用dumps包装下
		return HttpResponse(json.dumps(returnData))#render(request,'user_clients/user_clients.html',{'clients':clients})