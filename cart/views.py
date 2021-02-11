from django.shortcuts import render

from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.response import Response


from rest_framework.pagination import PageNumberPagination

from ecommerce_app.models import Product
from .models import Cart
from .serializers import CartSerializer ,QuantitySerializer


# Create your views here.

@api_view(["GET",])
@permission_classes((permissions.IsAuthenticated, ))
def GetAllProducts_in_cart(request):

    paginator_ForCart = PageNumberPagination()
    Cart_objects = Cart.objects.filter(user=request.user)
    result_page = paginator_ForCart.paginate_queryset(Cart_objects, request)
    serializer = CartSerializer(result_page,many=True)
    return paginator_ForCart.get_paginated_response(serializer.data)




@api_view(["PUT",])
@permission_classes((permissions.IsAuthenticated, ))
def update_quantity(request,pk):

    try:
        product = Cart.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if product.user != request.user:
        return Response({'response':"You don't have permission to edit that."})


    serializer = QuantitySerializer(product ,data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['quantity'] == 0: 
            return Response(data={"error":"you cannot set quantity to 0 if you want to delete the product click the delete button"})

        if serializer.validated_data['quantity'] > product.product.max_quantity :
            return Response(data={"error":"you cannot order more than " + str(product.product.max_quantity) })

        else :
            serializer.save()
        return Response(data={"succsess":"updated"})

    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST )


@api_view(["DELETE",])
@permission_classes((permissions.IsAuthenticated, ))
def delet_item_from_cart(request,pk):

    try:
        Carts = Cart.objects.get(pk=pk)
    except:
        return Response( status=status.HTTP_404_NOT_FOUND)

    if Carts.user != request.user:
        return Response({'response':"You don't have permission to delete that."}) 

    Carts.delete()
    return Response(data={"succsess":"deleted"})


@api_view(["POST",])
@permission_classes((permissions.IsAuthenticated, ))
def add_to_cart(request):

    Cart_create = Cart(user=request.user)
    serializer = CartSerializer(Cart_create,data=request.data)

    if serializer.is_valid():

        if  Cart.objects.filter(user=request.user).filter(product=serializer.validated_data['product']):
            return Response(data={"error":"this product is already on your cart if you want to edit quantity go to your cart "})
        else :
            if serializer.validated_data['quantity'] == 0: 
                return Response(data={"error":"you cannot set quantity to 0 "})
            
            x = Product.objects.get(name=serializer.validated_data['product']).max_quantity

            if serializer.validated_data['quantity'] > x :
                return Response(data={"error":"you cannot order more than " + str(x) })

            else :
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)