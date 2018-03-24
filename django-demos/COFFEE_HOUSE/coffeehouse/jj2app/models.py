from django.db import models
from datetime import date
from django.utils import timezone

from django.contrib.postgres.fields import ArrayField,JSONField

# Create your models here.
def default_city():
    return "San Diego"

class Store(models.Model):
    #id = models.AutoField(primary_key=True) # Added by default, not required explicitly
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=2, default='CA')
    #objects = models.Manager() # Added by default, not required explicitly

    #Values for fields that use the auto_now option are updated every time a record is changed, while
    #values for fields that use the auto_now_add option remain frozen for the lifetime of the record.
    date = models.DateField(default=date.today)
    datetime = models.DateTimeField(default=timezone.now)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s, %s)" % (self.name,self.city,self.state)


ITEM_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('P', 'Portion'),
        )

class Menu(models.Model):
    # 指定id为bigint自增,不自增的为models.BigIntegerField
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    field_array = ArrayField(models.IntegerField())
    field_json = JSONField()

class Item(models.Model):
    # 外键引用，级联删除貌似不起作用
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    size = models.CharField(choices=ITEM_SIZES, max_length=1)
    # blank表单允许空; null=True数据库允许为空.
    remark = models.CharField(max_length=20, blank=True, null=True)


