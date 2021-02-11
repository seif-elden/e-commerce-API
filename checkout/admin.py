from django.contrib import admin
from .models import OrderItem,order



class OrderItemAdmin(admin.TabularInline):
	'''
		Admin View for OrderItem
	'''
	model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
	'''
		Admin View for Order
	'''
	list_display = ('user','Address','created','deleverd')
	list_filter = ('deleverd','created')
	# search_fields = ['first_name','last_name','email']
	inlines = [
	OrderItemAdmin,
	]

admin.site.register(order, OrderAdmin)