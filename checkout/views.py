from django.shortcuts import render
from .models import order ,OrderItem
from accounts.models import Address
from cart.models import Cart
# Create your views here.


from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.response import Response

from .serializers import orderSerializer 


@api_view(["POST",])
@permission_classes((permissions.IsAuthenticated, ))
def add_to_order(request):
    cart = Cart.objects.filter(user=request.user)
    serializer = orderSerializer(data=request.data)

    if serializer.is_valid():

        if serializer.validated_data['Address'].user != request.user:
            return Response(data={"error":"your cannot use this address because it is not yours"})

        order__ = order.objects.create(
            user = request.user,
            Address = serializer.validated_data['Address']
        )
        for item in cart:
            OrderItem.objects.create(
                order=order__,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
                )
            item.delete()

        return Response(data={"succsess":"your order has been placed"})
       
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



