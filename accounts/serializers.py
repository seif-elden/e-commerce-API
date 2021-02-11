from rest_framework import serializers
from .models import Address
from django.contrib.auth.models import User


class AddressSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Address
        fields = '__all__'




class UserCreationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','password',"password2"]
        extra_kwargs ={
            "password":{'write_only' :True},
            "email" :{"required" : True},
            "first_name" :{"required" : True},
            "last_name" :{"required" : True}
        }

    def	save(self):
        account = User(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account

class UserDeatailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name']
        extra_kwargs ={
            "email" :{"required" : True ,"allow_blank":False},
            "first_name" :{"required" : True ,"allow_blank":False},
            "last_name" :{"required" : True ,"allow_blank":False},
        }

