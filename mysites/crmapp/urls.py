from django.conf.urls import url

from .views import (activate, activation_complete, register,
                    registration_closed, registration_complete)

urlpatterns = [
    url(r'^$', getuserclients, name='user_clients'),
    ]