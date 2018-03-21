from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^home/$', views.home),
    url(r'^method/$', views.method),

    url(r'^index-class$', views.AboutIndex.as_view(), {'onsale':True}),
    url(r'^contact-class$', views.ContactPage.as_view()),
]
