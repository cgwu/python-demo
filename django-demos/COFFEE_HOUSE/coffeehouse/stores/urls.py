from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^redirect$', views.redirect),
    url(r'^json$', views.json),
    url(r'^http$', views.http),
    url(r'^(?P<store_id>\d+)$', views.detail, name='detail'),
]
