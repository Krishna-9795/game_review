from rest_framework import serializers
from .models import Game, Review, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id','username')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
            
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
        
        
"""
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    
    def validate(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user or not user.is_superuser:
            raise serializers.ValidationError("Invalid credentials or not a superuser")
        return data
    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}

"""

