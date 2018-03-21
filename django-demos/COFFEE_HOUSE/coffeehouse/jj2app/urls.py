from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^foo$', views.foo),
    url(r'^django_foo_tpl$', TemplateView.as_view(template_name='django_foo_tpl.html')),
    url(r'^index$', TemplateView.as_view(template_name='jj2app/index.html')),
    url(r'^detail$', TemplateView.as_view(template_name='jj2app/detail.html')),
]
