from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly  # this allow user to view feed but not able to edit them even not authenticated as the feed user or other user
# this dosn't allows user to view others feed
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.

class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    # Filter options
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    # http_method_names = ['post', 'head']  # allos only post and head method

# Use Mod Header Chrome Extension to be authenticated and keep it disable when not in use
# The Mode Header has name and value
# Name: Authorization Value: Token <token generated when login>
# ! This is used for now in real life we use Python requests library for JS we use fetch library which use custom authntication token


class UserLoginApiView(ObtainAuthToken):
    """Handle creating User Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        # IsAuthenticatedOrReadOnly,  # can able to view feed even not authenticated
        IsAuthenticated,  # can't able to view feed
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ImageItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    http_method_names = ['get', 'head']
