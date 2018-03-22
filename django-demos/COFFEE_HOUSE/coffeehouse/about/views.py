from django.shortcuts import render

from django.http import HttpResponsePermanentRedirect, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import TemplateView, View

from .models import ContactForm

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
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/about/contact/thankyou')
        else:
            pass # is_valid() method created errors dict, can access from form.errors in a template.
    else:
        # GET, generate blank form
        form = ContactForm()
        #form = ContactForm(initial={'email':'johndoe@coffeehouse.com','name':'John Doe'}) # 有初始值
    return render(request, 'about/contact.html', {'form':form})

def home(request):
    return HttpResponsePermanentRedirect(reverse('homepage'))

def method(request):
    return HttpResponsePermanentRedirect(reverse('drink', args=(drink.name,)))


#CLASS BASED VIEW
class AboutIndex(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutIndex, self).get_context_data(**kwargs)
        context['aboutdata'] = 'Custom data<>&'
        return context

#Class-based view inherited from View with multiple HTTP handling
class ContactPage(View):
    mytemplate = 'about/contact.html'
    unsupported = 'Unsupported operation'

    def get(self, request):
        return render(request, self.mytemplate)

    def post(self, request):
        return HttpResponse(self.unsupported)


