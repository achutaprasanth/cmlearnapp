from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.static import serve
from django.conf import settings

from . import views

router = DefaultRouter()
# this is the basic list view that displayed inbrowser
# `viewsetsInUrls` is the URL prefix appears in url
# so to do opeartion like retrive, put,patch,destroy we need to enter primary key(pk) at the end of the url
router.register('profileViewSet', views.UserProfileViewSets,
                basename='profileViewSet')
# the basename is to add or override the 'queryset'(in views.py) in a viewset

router.register('imageviewset', views.ImageViewSet, basename='imageviewset')

router.register('feed', views.UserProfileFeedViewSet, basename='profileFeed')

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    url(r'viewsets/', include(router.urls)),
    url(r'^(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
]
