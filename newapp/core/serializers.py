from rest_framework import serializers
from . import models
from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=False)


class UserProfileSerializer(serializers.ModelSerializer):
    """This ModelSerializer has advantages of interacting with Django model"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serialize profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'image', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


class ImageItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'image', 'created_on', 'image_url')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }

    def get_image_url(self, obj):
        a =  obj.image.url
        print(a)
        try:
            b = a.split('/media_in/')
            c = b[0]+'/media_out/out_'+b[1]
        except IndexError:
            c = a
        return c
