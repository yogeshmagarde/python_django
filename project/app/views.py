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
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

def hello_geeks (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")


def login_page(request):
    return render(request, "app/login.html")

def register_page(request):
    return render(request, "app/register.html")

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch") 
class UserSignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token = Token.objects.create(user=user)
            return Response({"ack": "User registerd successfully...","token":token.key}, status= status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    

@method_decorator(csrf_exempt, name="dispatch") 
class loginview(APIView):
    def post(self, request, *args, **kwargs):
        serializer = loginserializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                token = Token.objects.get(user=user)
                request.session["username"] = user.username  # Store username in session
                request.session["key"] = token.key
                return Response({"message":"login successfuly", "username": user.username, "token":token.key})
            else:
                return Response({"message":"wrong username password"})
        return Response(serializer.errors)

    
class Profile_View(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        current_user = request.user
        users_id = User.objects.get(username= current_user).id
        profile = Profile.objects.create(user_id=users_id, image=request.FILES.get('image'))
        profile.save()
        return Response({"ack": "User image uploaded successfully..."}, status= status.HTTP_201_CREATED)
    

    def put(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = user.profile
            print(profile)  # Access the related Profile object
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Profile_updateserializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ack": "User profile updated successfully..."}, status= status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    