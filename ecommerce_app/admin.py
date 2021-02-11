from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ("name",)


admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    fields = ('category','name','Image','description','price','max_quantity','available',)
    list_display = ('name','category','price','max_quantity','available','created',)
    list_filter = ('available','created','category',)
    list_editable = ('price','max_quantity','available',)


admin.site.register(Product, ProductAdmin)