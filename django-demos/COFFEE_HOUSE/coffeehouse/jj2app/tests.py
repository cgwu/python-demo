from django.test import TestCase,TransactionTestCase
#from django.test.utils import override_settings
#from django.db import transaction
import time
import unittest
from django.db import connection

#from coffeehouse.jj2app.models import Store
from .models import Store

# Create your tests here.
# ref:  https://docs.djangoproject.com/en/1.11/topics/testing/overview/
#       https://www.jianshu.com/p/34267dd79ad6
# 启动测试: ./manage.py test coffeehouse.jj2app.tests.StoreTestCase --keepdb

#import logging
#LOG = logging.getLogger(__name__)

class StoreTestCase(TestCase):
#class StoreTestCase(TransactionTestCase):
    def setUp(self):
#        LOG.debug('=== setup ===')
        print('启动设置setup ...')
        Store.objects.create(name='大郎烧饼8', address='沉香street#8') # Create

    #@transaction.commit_on_success
    #@override_settings(DEBUG=False)
    def test_save(self):
#        LOG.debug('test save store')
        print('test save store')
        store1 = Store(name='大郎烧饼', address='沉香street#1')
        #with transaction.commit_on_success():
        store1.save()  # create or update
        print('#id', store1.id)
        #time.sleep(60)

    def tearDown(self):
#        LOG.debug('=== tear down ===')
        print('销毁测试!')

# 从此处继承，运行测试用例后会保存数据
# ./manage.py test coffeehouse.jj2app.tests.StoreUnitTestCase.test_save -k
class StoreUnitTestCase(unittest.TestCase):
    def test_save(self):
        #store1 = Store.objects.create(name='烧J店2', address='street2号') # Create
        #store1 = Store(name='烧J店2 a very long name', address='street2号') # Create
        store1 = Store(name='烧J店2 a very long name', address='street5号', city='San Diego', state='CA')
        store1.clean_fields()       # 验证字段集
        store1.validate_unique()    # 验证唯一性
        store1.clean()              # 自定义验证
        store1.save()
        print('#id', store1.id)

    def test_delete(self):
        #ret = Store.objects.delete(id=18)
        store_del = Store(id=18)
        ret = store_del.delete()
        print(ret)

    def test_refresh_from_db(self):
        store_refresh = Store(id=27)
        store_refresh.refresh_from_db()
        print(store_refresh)

    def test_get(self):
        res = Store.objects.get(id=27)
        print(res)

    def test_delete_all(self):
        ret = Store.mgr.all().delete()
        print(ret)

    # 执行原生sql: https://blog.csdn.net/kelindame/article/details/52443972
    def test_rawsql_getone(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from jj2app_store where id = %s", [31])
            ret = cursor.fetchone()
            print(ret)

    def test_rawsql_delete(self):
        with connection.cursor() as cursor:
            ret  = cursor.execute("delete from jj2app_store where id = %s", [30])
            print('delete ret:',ret)

