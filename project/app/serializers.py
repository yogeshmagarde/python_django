from django.contrib.auth.models import User
from app.models import Profile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validate_data):
        user = User.objects.create(username=validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user


class loginserializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 255)
    password = serializers.CharField(max_length = 255)
    class Meta:
        model = User
        fields = ['username','password']


class Profile_updateserializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        # read_only_fields = ["user"]

