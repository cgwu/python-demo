from django.shortcuts import render

from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import TemplateView, View

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


#CLASS BASED VIEW
class AboutIndex(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutIndex, self).get_context_data(**kwargs)
        context['aboutdata'] = 'Custom data'
        return context

#Class-based view inherited from View with multiple HTTP handling
class ContactPage(View):
    mytemplate = 'about/contact.html'
    unsupported = 'Unsupported operation'

    def get(self, request):
        return render(request, self.mytemplate)

    def post(self, request):
        return HttpResponse(self.unsupported)


