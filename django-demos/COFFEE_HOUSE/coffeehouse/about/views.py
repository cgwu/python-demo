from django.shortcuts import render

from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    # Shortcut level methods
    sqlqueries = 'select * from foo'
    messages.debug(request, 'debug: The following SQL statements were executed: %s' % sqlqueries) # Debug messages ignored by default
    messages.info(request, 'info: All items on this page have free shipping.')
    messages.success(request, 'success: Email sent successfully.')
    messages.warning(request, 'warning: You will need to change your password in one week.')
    messages.error(request, 'error: We could not process your request at this time.')
    #messages.set_level(request, messages.WARNING) # NOT working yet
    return render(request, 'about/contact.html')

def home(request):
    return HttpResponsePermanentRedirect(reverse('homepage'))

def method(request):
    return HttpResponsePermanentRedirect(reverse('drink', args=(drink.name,)))
