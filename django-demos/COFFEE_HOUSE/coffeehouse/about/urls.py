from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^home/$', views.home),
    url(r'^method/$', views.method),

    url(r'^index-class$', views.AboutIndex.as_view(), {'onsale':True}),
    url(r'^contact-class$', views.ContactPage.as_view()),

    url(r'^share/index$', TemplateView.as_view(template_name='share/index.html')),
    url(r'^share/detail$', TemplateView.as_view(template_name='share/detail.html')),
]
