from django.shortcuts import render

# Create your views here.
def index(request,store_id='1'):
    return render(request, 'stores/detail.html', {'location':'headquarters', 'store_id':store_id})

def detail(request, store_id='1', location=None):
    # ?hours=sunday&maps=flash
    hours = request.GET.get('hours','')
    maps = request.GET.get('maps','')
    return render(request, 'stores/detail.html',
            {'store_id': store_id,'location':location,'hours':hours,'maps':maps})


