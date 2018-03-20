from django.shortcuts import render

from django.http import HttpResponsePermanentRedirect, JsonResponse, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request,store_id='1',location=None):
    return render(request, 'stores/detail.html', {'location':'headquarters', 'store_id':store_id,'location':location})

def detail(request, store_id='1', location=None):
    # ?hours=sunday&maps=flash
    hours = request.GET.get('hours','')
    maps = request.GET.get('maps','')
    return render(request, 'stores/detail.html',
            {'store_id': store_id,'location':location,'hours':hours,'maps':maps})

# Redirect to about:index page.
def redirect(request, location=None):
    return HttpResponsePermanentRedirect(reverse('about:index'))

def json(request, location=None):
    data_dict = {'name':'dannis', 'age':30}
    return JsonResponse(data_dict)

def http(request, location=None):
    return HttpResponse('<h4>Django inline response</h4>')

