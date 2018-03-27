from django.contrib import admin
from .models import CoffeehouseUser

# Register your models here.
class CoffeehouseUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CoffeehouseUser, CoffeehouseUserAdmin)

