from django.db import models

from django.contrib.auth.models import User
from accounts.models import Address
from ecommerce_app.models import Product


from django.db.models.signals import post_save
from django.dispatch import receiver

class order(models.Model):

    user = models.ForeignKey(User,related_name='Order',on_delete=models.CASCADE) 
    Address   = models.ForeignKey(Address,related_name='items',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    deleverd = models.BooleanField(default=False)
    total_oreder_cost = models.PositiveIntegerField(null=True,default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return  str(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order   = models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product  = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price   = models.DecimalField(max_digits=10,decimal_places=2)
    quantity    = models.PositiveIntegerField(default=0)
    total_item_cost = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"


    def __str__(self):
        return str(self.pk)

    def save(self,*args, **kwargs):
        self.total_item_cost = self.price * self.quantity
        return super(OrderItem,self).save(*args, **kwargs)


@receiver(post_save, sender=OrderItem)
def get_total_oreder_cost(sender, instance=None, created=False, **kwargs):
    if created:
        instance.order.total_oreder_cost += instance.total_item_cost
        instance.order.save()

    