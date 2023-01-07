from django.urls import include, re_path
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'message', MessagePostViewSet, basename='message')

urlpatterns =[
    
 
    path('', include(router.urls))
]