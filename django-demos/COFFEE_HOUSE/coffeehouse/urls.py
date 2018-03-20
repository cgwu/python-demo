"""coffeehouse URL Configuration

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
from django.views.generic import TemplateView

#from coffeehouse.about import views as about_views
#from coffeehouse.stores import views as stores_views

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^drinks/(?P<drink_name>\D+)$', TemplateView.as_view(template_name='drinks/index.html'), {'onsale':False}),

    #url(r'^about/$', about_views.contact),
    #url(r'^about/index/$', TemplateView.as_view(template_name='index.html')),
    url(r'^about/', include('coffeehouse.about.urls')),

    #url(r'^stores/$', stores_views.detail, {'location':'headquarters'}),
    #url(r'^stores/(?P<store_id>\d+)$', stores_views.detail),
    url(r'^stores/', include('coffeehouse.stores.urls')),

]
