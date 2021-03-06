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

from django.conf import settings

#from coffeehouse.about import views as about_views
#from coffeehouse.stores import views as stores_views

# ref: http://django-rest-swagger.readthedocs.io/en/latest/
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CoffeeHouse API')

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')), # all auth package
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"),

    #url(r'^drinks/(?P<drink_name>\D+)/$', TemplateView.as_view(template_name='drinks/index.html'), {'onsale':False}, name='drink'),
    url(r'^drinks/(?P<drink_name>\D+)/$', TemplateView.as_view(template_name='drinks/index.html'), name='drink'),

    #url(r'^about/$', about_views.contact),
    #url(r'^about/index/$', TemplateView.as_view(template_name='index.html')),
    url(r'^about/', include('coffeehouse.about.urls', namespace='about')),

    #url(r'^stores/$', stores_views.detail, {'location':'headquarters'}),
    #url(r'^stores/(?P<store_id>\d+)$', stores_views.detail),
    url(r'^stores/', include('coffeehouse.stores.urls', namespace='stores'), {'location':'headquarters'}),

    url(r'^jj2app/', include('coffeehouse.jj2app.urls', namespace='jj2app')),
    # /rest-auth/login
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-doc$', schema_view),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


