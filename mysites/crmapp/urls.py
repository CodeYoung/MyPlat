# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import (getuserclients, adduserclient,userclient,searchUserClients,editclient,deleteclient,managecontacts)

urlpatterns = [
    url(r'^getuserclients$', getuserclients, name='user_clients'),
    url(r'^addclient$',adduserclient,name='user_addclient'),
    url(r'^userclient$',userclient,name='userclient'),
    url(r'^userclientdata$',searchUserClients,name='userclientdata'),
    url(r'^editclient$',editclient,name='editclient'),
    url(r'^deleteclient/(\d+)/$',deleteclient,name='deleteclient'),
    url(r'^managecliencontacts$',managecontacts,name='managecontacts')
    ]