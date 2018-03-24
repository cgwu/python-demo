from django.test import TestCase,TransactionTestCase
from django.db import transaction

#from coffeehouse.jj2app.models import Store
from .models import Store

# Create your tests here.
# ref:  https://docs.djangoproject.com/en/1.11/topics/testing/overview/
#       https://www.jianshu.com/p/34267dd79ad6
# 启动测试: ./manage.py test coffeehouse.jj2app.tests.StoreTestCase --keepdb

#import logging
#LOG = logging.getLogger(__name__)

#class StoreTestCase(TestCase):
class StoreTestCase(TransactionTestCase):
    def setUp(self):
#        LOG.debug('=== setup ===')
        print('启动设置setup ...')

    #@transaction.commit_on_success
    def test_save(self):
#        LOG.debug('test save store')
        print('test save store')
        store1 = Store(name='大郎烧饼', address='沉香street#1')
        #with transaction.commit_on_success():
        store1.save()
        print('#id', store1.id)

    def tearDown(self):
#        LOG.debug('=== tear down ===')
        print('销毁测试!')

