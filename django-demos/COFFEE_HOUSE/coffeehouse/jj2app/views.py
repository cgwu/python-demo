from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.forms import formset_factory

#from django.views.generic.edit import CreateView
#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
# 从下面空间全部导入
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy

# Python logging package
import logging
# Standard instance of a logger with __name__
LOG = logging.getLogger(__name__)

from coffeehouse.about.models import ContactForm,ContactCommentOnlyForm
from .models import Store, StoreForm, MenuItem, MenuItemForm
from .forms import DrinkForm

# Create your views here.
def drink(request):
    extra_forms = 2
    # extra参数,额外的表单个数(2代表共3个表单);max_num最多表单数.
    #formset_factory(form, formset=BaseFormSet, extra=1, can_order=False, can_delete=False,
    #   max_num=None, min_num=None, validate_max=False, validate_min=False)
    DrinkFormSet = formset_factory(DrinkForm, extra=extra_forms, max_num=20)
    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy ['form-TOTAL_FORMS']) + extra_forms
            formset = DrinkFormSet(formset_dictionary_copy)
        else:
            formset = DrinkFormSet(request.POST)
            if formset.is_valid():
                #LOG.info(formset)
                return HttpResponse('保存成功!')
    else:
        formset = DrinkFormSet(initial=[{'name':1, 'size':'m', 'amount': 1}])
    return render(request, 'jj2app/drink.html', {'formset': formset})



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


# Django class-based view with CreateView to create model records
class MenuItemCreation(CreateView):
    template_name = 'jj2app/menuitem_custom_form.html' # 自定义表单名,默认为jj2app/menuitem_form.html
    context_type='text/html'
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy('jj2app:menu-item-list')

    def get_context_data(self,**kwargs):
        kwargs['special_context_variable'] = 'My special context variable!!!'
        context = super(MenuItemCreation, self).get_context_data(**kwargs)
        return context

class MenuItemList(ListView):
    model = MenuItem
    ordering = ['id']

class MenuItemDetail(DetailView):
    model = MenuItem

class MenuItemUpdate(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy('jj2app:menu-item-list')

class MenuItemDelete(DeleteView):
    model = MenuItem
    form_class = MenuItemForm
    success_url = reverse_lazy('jj2app:menu-item-list')

