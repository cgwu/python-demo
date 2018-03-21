from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = staticfiles_storage.url
        self.globals['reverse'] = reverse
        self.globals['global_msg'] = 'Global Message' # for test

