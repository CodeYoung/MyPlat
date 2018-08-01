from django.conf.urls import url

from .views import (getuserclients, adduserclient,userclient,searchUserClients,editclient,deleteclient)

urlpatterns = [
    url(r'^getuserclients$', getuserclients, name='user_clients'),
    url(r'^addclient$',adduserclient,name='user_addclient'),
    url(r'^userclient$',userclient,name='userclient'),
    url(r'^userclientdata$',searchUserClients,name='userclientdata'),
    url(r'^editclient/(\d+)/$',editclient,name='editclient'),
    url(r'^deleteclient/(\d+)/$',deleteclient,name='deleteclient')

    ]