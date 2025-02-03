from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from app.serializers import UserSerializer, loginserializer, Profile_updateserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

def hello_geeks (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")

# Create your views here.
class UserSignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        print(serializer,"serializer")
        if serializer.is_valid():
            user=serializer.save()
            token = Token.objects.create(user=user)
            return Response({"ack": "User registerd successfully...","token":token.key}, status= status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    

    
class loginview(APIView):
    def post(self, request, *args, **kwargs):
        serializer = loginserializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                return Response({"message":"login successfuly"})
            else:
                return Response({"message":"wrong username password"})
        return Response(serializer.errors)

    
class Profile_View(APIView):
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
    
        users_id = User.objects.get(username= current_user).id
        
        print(users_id)
        profile = Profile.objects.create(user_id=users_id, image=request.FILES.get('image'))
        profile.save()
        return Response({"ack": "User image uploaded successfully..."}, status= status.HTTP_201_CREATED)
    
