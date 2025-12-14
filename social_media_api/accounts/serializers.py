from rest_framework import serializers
from .models import SocialMediaAccount
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token serializers.CharField(), Token.objects.create, get_user_model().objects.create_user

class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccount
        fields = ['bio', 'profille_picture', 'followers']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


