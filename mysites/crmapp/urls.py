from django.conf.urls import url

from .views import (getuserclients, adduserclient)

urlpatterns = [
    url(r'^$', getuserclients, name='user_clients'),
    url(r'/addclient^$',adduserclient,name='user_addclient'),

    ]