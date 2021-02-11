from rest_framework import serializers
from .models import order , OrderItem



class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = ["Address",]


