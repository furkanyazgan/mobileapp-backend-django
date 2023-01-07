from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.decorators import action 
from rest_framework.response import Response
import json
from .serializers import *
from django.core import serializers as dj_serializers
#{"name":"furkan","surname":"yazgan","email":"furkan@gmail.com","password":"123123"}

class AuthViewSet(viewsets.ViewSet):

    
    @action(detail=False,methods=["POST"],url_path="create")
    def CreateUserAccount(self,request):        
        try:

            serializer = CreateUserAccountSerializer(data=request.data)
            print(request.data)
            if(serializer.is_valid(raise_exception=True)):      
                print("validmiş")                     
                serializer.save()                
                return Response(data=json.dumps({"status": "succesful", "is_success": True,"message": "successfully added data.", "data": {"id":serializer.data["id"] }}), status=status.HTTP_200_OK)
            else:
                return Response(data=json.dumps({'status': "error","is_success": False, "message": "invalid user form"}), status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response(data=json.dumps({'status': "unsuccessful","is_success": False, 'message': str(e)}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    @action(detail=False, methods=['post'], url_path='get')
    def GetUserAccount(self,request):
         
        try:
            serializer = GetUserAccountSerializer(data=request.data)
            if (serializer.is_valid(raise_exception=True)):
                Id = serializer.data['id']
                EmissionFactorValuesModel = UserAccount.objects.get(pk=int(Id))
                EmissionFactorValuesModel_json = dj_serializers.serialize(
                    "json", [EmissionFactorValuesModel, ])
                return Response(data=json.dumps({"status": "succesful", "message": "Fetched line data successfully.", "data": EmissionFactorValuesModel_json}), status=status.HTTP_200_OK)
            else:
                return Response(data=json.dumps({"status": "unsuccessful", "message": "request body is not valid"}), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=json.dumps({'status': "unsuccessful", 'message': str(e)}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], url_path='login')
    def LoginUserAccount(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]

            userAccountModel = UserAccount.objects.filter(email=email).first()
            
            if userAccountModel is None:
                return Response(data=json.dumps({'status': "error", "is_success": False, "message": "UserAccount not found"}), status=status.HTTP_200_OK)
            
            if not userAccountModel.password == password:
                return Response(data=json.dumps({'status': "error", "is_success": False, "message": "email or password is incorrect"}), status=status.HTTP_200_OK)

            

            return Response(data=json.dumps({'status': "successful", "is_success": True, "message": "Login Successful.", "data": {"id" :userAccountModel.id}}), status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(data=json.dumps({'status': "error", "is_success": False, "message": str(e)}), status=status.HTTP_200_OK)


       



 
    



class MessagePostViewSet(viewsets.ViewSet):
    @action(detail=False,methods=["POST"],url_path="create")
    def CreateMessagePost(self,request):        
        try:

            serializer = CreateMessagePostSerializer(data=request.data)
            print(request.data)
            if(serializer.is_valid(raise_exception=True)):                           
                serializer.save()                
                return Response(data=json.dumps({"status": "succesful", "is_success": True,"message": "successfully added data." }), status=status.HTTP_200_OK)
            else:
                return Response(data=json.dumps({'status': "error","is_success": False, "message": "invalid user form"}), status=status.HTTP_200_OK)
        
        except Exception as e:

            return Response(data=json.dumps({'status': "unsuccessful","is_success": False, 'message': str(e)}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['get'], url_path='get_all')
    def getAllEmissionFactorValues(self,request):
        try:
            print(MessagePost.objects.all())
            MessagePostModel_json = dj_serializers.serialize(
                "json", MessagePost.objects.all())

            dataJson = {"status": "success",
                        "message": "successfully fetched all data", "data": MessagePostModel_json}
            return Response(data=json.dumps(dataJson), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=json.dumps({'status': "unsuccessful", 'message': str(e)}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)