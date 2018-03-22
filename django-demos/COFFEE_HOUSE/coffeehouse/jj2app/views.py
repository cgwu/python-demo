from django.shortcuts import render
# Python logging package
import logging
# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

# Create your views here.
def foo(request):
    stdlogger.warning('您访问了jj2app/foo!')
    return render(request, 'jj2app/foo.html')

