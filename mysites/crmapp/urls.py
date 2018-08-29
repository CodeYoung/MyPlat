# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import * #(getuserclients, adduserclient,userclient,searchUserClients,editclient,deleteclient,managecontacts,searchclientcontacts,addClientContacts,clientContacts)

urlpatterns = [
    url(r'^getuserclients$', getuserclients, name='user_clients'),
    url(r'^addclient$',adduserclient,name='user_addclient'),
    url(r'^userclient$',userclient,name='userclient'),
    url(r'^userclientdata$',searchUserClients,name='userclientdata'),
    url(r'^editclient/(\d+)/$',editclient,name='editclient'),
    url(r'^deleteclient/(\d+)/$',deleteclient,name='deleteclient'),
    url(r'^managecliencontacts$',managecontacts,name='managecontacts'),
    url(r'^clientcontactsdata$',searchclientcontacts,name='searchclientcontacts'),
    url(r'^addClientContacts$',addClientContacts,name='addClientContacts'),
    url(r'^clientContacts$',clientContacts,name='clientContacts'),
    url(r'^deleteContacts/(\d+)/$',deleteContacts,name='deleteContacts'),
    url(r'^editContacts/(\d+)/$',editContacts,name='editContacts'),
    
    ]