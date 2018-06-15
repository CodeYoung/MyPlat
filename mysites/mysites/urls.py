"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import view,search,add
from basemodel import views as basemodel

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$',view.hello),
    #url(r'^searchOrganization$',organization.searchOrganization),
    url(r'^search$', search.search),
    #url(r'^addOrganization$',organization.addOrganization),
    url(r'^index.html$',view.index),
    url(r'^test.html',view.test),
    url(r'^add$',add.add),
    url(r'^base/', include('basemodel.urls')),
    url(r'^$',basemodel.index),
    url(r'^accounts/',include('users.urls')),
    url(r'^accounts/profile/',basemodel.accounts_profile),

    #url(r'^head.jpg',include('static.img.head.jpg')),


]
