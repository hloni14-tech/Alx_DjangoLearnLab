from rest_framework import serializers
from .models import SocialMediaAccount
from django.contrib.auth.models import User

class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccount
        fields = ['bio', 'profille_picture', 'followers']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


