from rest_framework import serializers
from .models import *

class CreateUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["id","email","name","surname","password"]

class GetUserAccountSerializer(serializers.Serializer):
    id = serializers.FloatField(required=True)



class CreateMessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagePost
        fields = ["message","name"]