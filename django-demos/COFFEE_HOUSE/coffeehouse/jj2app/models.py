from django import forms
from django.db import models
from datetime import date
from django.utils import timezone

from django.contrib.postgres.fields import ArrayField,JSONField
# Import built-in validator
from django.core.validators import MinLengthValidator
# Create custom validator
from django.core.exceptions import ValidationError

def calorie_watcher(value):
    if value > 5000:
        raise ValidationError(
                ('Whoa! calories are %(value)s ? We try to server healthy food, try something less than 5000!'),
                params = {'value': value}
        )
    if value < 0:
        raise ValidationError(
            ('Strange calories are %(value)s ? This can\'t be, value must be greater than0'),
            params={'value': value}
        )

# Create your models here.
def default_city():
    return "San Diego"

class Store(models.Model):
    #id = models.AutoField(primary_key=True) # Added by default, not required explicitly
    name = models.CharField(max_length=30, validators=[MinLengthValidator(5)])
    address = models.CharField(max_length=30, unique=True)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=2, default='CA')
    #objects = models.Manager() # Added by default, not required explicitly
    mgr = models.Manager() # Default model manager rename

    #Values for fields that use the auto_now option are updated every time a record is changed, while
    #values for fields that use the auto_now_add option remain frozen for the lifetime of the record.
    date = models.DateField(default=date.today)
    datetime = models.DateTimeField(default=timezone.now)
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    # 自定义验证
    def clean(self):
        # Don't allow 'San Diego' city entries that have state different than 'CA'
        if self.city == 'San Diego' and self.state != 'CA':
            raise ValidationError('Wait San Diego is CA!, are you sure there is another San Diego in %s ?'
                % self.state)

    def __str__(self):
        return "id: %s, name: %s, city: %s, state: %s" % (str(self.id), self.name,self.city,self.state)

    class Meta:
        ordering = ['-state'] # orders the results by the state field in descending order.
        # If you want to disable Django executing a model’s default DDL
        # against a database, you can do so with meta managed=False option. The managed=False option is useful
        # when a model’s backing database table is created by some other means and you don’t want Django to
        # interfere with the management of this table.
        indexes = [
            models.Index(fields=['city','state']),
            models.Index(fields=['city'], name='city_idx')
        ]
        # The meta abstract option allows a Django model to function as a base class
        # that doesn’t have a backing database table,
        # but serves as a foundation for other Django model classes.
        # abstract = True

# 生成与Model对应的表单
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

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

# Database Definition Language (DDL) Values: db_column, db_index, db_tablespace, primary_key
class Item(models.Model):
    # 外键引用，级联删除貌似不起作用
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # P293: Form Values: Editable, help_text, verbose_name, and error_messages
    name = models.CharField(max_length=30, verbose_name="ITEM NAME", validators=[MinLengthValidator(5)])
    description = models.CharField(max_length=100, help_text="Ensure you provide some desc")
    size = models.CharField(choices=ITEM_SIZES, max_length=1)
    # blank表单允许空; null=True数据库允许为空.
    remark = models.CharField(max_length=20, blank=True, null=True)
    calories = models.IntegerField(null=True, validators=[calorie_watcher])

