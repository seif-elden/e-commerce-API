from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination


from .models import Product , Category
from .serializers import ProductSerializer ,CategorySerializer

# Create your views here.

@api_view(["GET",])
@permission_classes([])
@authentication_classes([])
def GetAllProducts(request):

    paginator_ForProduct = PageNumberPagination()
    Product_objects = Product.objects.all()
    result_page = paginator_ForProduct.paginate_queryset(Product_objects, request)
    serializer = ProductSerializer(result_page,many=True)
    return paginator_ForProduct.get_paginated_response(serializer.data)


@api_view(["GET",])
@permission_classes([])
@authentication_classes([])
def GetOneProducts(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["GET",])
@permission_classes([])
@authentication_classes([])
def Get_Categories(request):
    try:
        categories = Category.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET",])
@permission_classes([])
@authentication_classes([])
def GetProducts_InCategory(request,pk):
    try:
        product = Product.objects.filter(category=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)