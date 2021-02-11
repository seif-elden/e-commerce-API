from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from .models import Address
from .serializers import UserCreationSerializer , AddressSerializer , UserDeatailsSerializer

# Create your views here.




# ADDRESS VIEWS

@api_view(["GET",])
@permission_classes((permissions.IsAuthenticated, ))
def GetAllAddress(request):

    all_address = Address.objects.filter(user=request.user)
    serializer = AddressSerializer(all_address,many=True)
    return Response(serializer.data)


@api_view(["GET",])
@permission_classes((permissions.IsAuthenticated, ))
def api_get_address(request,pk):

    try:
        address = Address.objects.get(pk=pk)
    except:
        return Response(data={'Address':"couldn't find address"},status=status.HTTP_404_NOT_FOUND)

    if address.user != request.user:
        return Response({'response':"You don't have permission to viwe that."}) 

    serializer = AddressSerializer(address)
    return Response(serializer.data)


@api_view(["PUT",])
@permission_classes((permissions.IsAuthenticated, ))
def api_edit_address(request,pk):

    try:
        addres = Address.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if addres.user != request.user:
        return Response({'response':"You don't have permission to edit that."}) 
    serializer = AddressSerializer(addres ,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={"succsess":"updated"})

    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST )


@api_view(["DELETE",])
@permission_classes((permissions.IsAuthenticated, ))
def api_delet_address(request,pk):

    try:
        address = Address.objects.get(pk=pk)
    except:
        return Response(data={'Address':"couldn't find address"},status=status.HTTP_404_NOT_FOUND)
    if address.user != request.user:
        return Response({'response':"You don't have permission to delete that."}) 
    status_of_deleting = address.delete()

    if status_of_deleting :
        return Response(data={"succsess":"deleted"})
    else:
        return Response(data={"failed":"failed couldnot delete"})


@api_view(["POST",])
@permission_classes((permissions.IsAuthenticated, ))
def api_add_address(request):

    address_create = Address(user=request.user)
    serializer = AddressSerializer(address_create,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







#  USER VIEWS

@api_view(["POST",])
@permission_classes([])
@authentication_classes([])
def CreatUser(request):

    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key
        data = {"token":token}
        data.update(serializer.data)
        return Response(data=data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT",])
@permission_classes((permissions.IsAuthenticated, ))
def Edit_User(request):

    serializer = UserDeatailsSerializer(request.user ,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"succsess":"updated"})

    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST )


@api_view(["GET",])
@permission_classes((permissions.IsAuthenticated, ))
def GET_User(request):

    serializer = UserDeatailsSerializer(request.user)
    return Response(serializer.data)
