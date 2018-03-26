from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse, HttpResponseRedirect
from django.db import transaction
# Python logging package
import logging
# Standard instance of a logger with __name__
LOG = logging.getLogger(__name__)

from coffeehouse.about.models import ContactForm,ContactCommentOnlyForm
from .models import Store, StoreForm

# Create your views here.
'''
Django supports the ATOMIC_REQUESTS option that is "disabled by default".
The ATOMIC_REQUEST is used to open
a transaction on every request made to a Django application.

Selectively activate and deactivate atomic requests with @non_atomic_requests and @atomic
'''
@transaction.atomic
def foo2(request):
    LOG.warning('您访问了jj2app/foo!')
    store1 = Store(name='大郎烧饼1', address='沉香street#1')
    store1.save() #测试保存到数据库成功
    store2 = Store(name='大郎烧饼2', address='沉香street#2')
    store2.save() #测试保存到数据库成功
    return render(request, 'jj2app/foo.html')

def foo(request):
    street_id = request.GET.get('street_id')
    LOG.warning('您访问了jj2app/foo! street id: %s' % street_id)
    # 上面可以是一个独立的事务
    # Open new transaction with context manager
    with transaction.atomic():
        store1 = Store(name='大郎烧饼10', address='沉香street#3'+street_id)
        store1.save() #测试保存到数据库成功
        #store2 = Store(name='大郎烧饼20', address='沉香street#4')
        #store2.save() #测试保存到数据库成功
    # 下面可以开启另一个新事务
    return render(request, 'jj2app/foo.html')

def contact(request):
    #form = ContactForm()
    #return render(request, 'jj2app/contact.html', {'form':form})
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('<h1>thank you!</h1>')
        else:
            pass
    else:
        form = ContactForm()
        partialForm = ContactCommentOnlyForm()
    return render(request, 'jj2app/contact.html', {'form':form, 'partialForm': partialForm })

def store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save() # 保存模型到数据库
            return HttpResponse('<h1>thank you!</h1>')
        else:
            pass
    else:
        form = StoreForm()
    return render(request, 'jj2app/store.html', {'form':form})

