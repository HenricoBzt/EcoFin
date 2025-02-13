from django.contrib import admin
from finances.models import Category
from finances.models import Expense

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','describe','value','categoryfk','date',)
    list_filter = ['categoryfk','date']
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)

