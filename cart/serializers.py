from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    product_name = serializers.ReadOnlyField(source='product.name')
    product_Image = serializers.ReadOnlyField(source='product.Image.url')
    product_description = serializers.ReadOnlyField(source='product.description')
    product_price = serializers.ReadOnlyField(source='product.price')
    product_max_quantity  = serializers.ReadOnlyField(source='product.max_quantity')
    class Meta:
        model = Cart
        fields = ['pk','user','product', "product_name",'quantity','product_price','product_description','product_Image',"product_max_quantity"]



class QuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['quantity']

