from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse, HttpResponseRedirect
# Python logging package
import logging
# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

from coffeehouse.about.models import ContactForm,ContactCommentOnlyForm
from .models import Store

# Create your views here.
def foo(request):
    stdlogger.warning('您访问了jj2app/foo!')
    #store1 = Store(name='大郎烧饼', address='沉香street#1')
    #store1.save() #测试保存到数据库成功
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

