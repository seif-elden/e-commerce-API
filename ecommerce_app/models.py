from django.db import models
from django.utils.text import slugify
from django.contrib import messages
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=200,db_index=True,unique=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category,self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.slug




class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    Image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    max_quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id','slug'),)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args, **kwargs)
        

    def __str__(self):
        return self.name




