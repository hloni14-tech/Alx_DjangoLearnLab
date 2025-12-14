from django.http import JsonResponse


def register_view(request):
	return JsonResponse({'message': 'register endpoint'})


def login_view(request):
	return JsonResponse({'message': 'login endpoint'})


def profile_view(request):
	return JsonResponse({'message': 'profile endpoint'})

def follow_view(request):
	return JsonResponse({'message': 'follow endpoint'})

def unfollow_view(request):
	retun JsonResponse({'message': 'unfollow endpoint'})

from generics.GenericAPIView import GnericAPIView
from rest_framework.response import Response
from rest_framework import permissions

class SampleGenericView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

	def get_customers(request): 
        return CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a sample generic view response."})

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
]

