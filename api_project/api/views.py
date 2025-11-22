from rest_framework import generics
from .models import Book, MyModel
from .serializers import BookSerializer, MyModelSerializer
from rest_framework import .viewsets.ModelViewSet
from rst_framework.permissions import obtain_auth_token

class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSetModelViewSet(generics.ModelViewSet):

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):
    permission_classes = [IsAuthenticated]  
    
    def get(self, request):
        return Response({
            "message": f"Welcome, {request.user.username} ( you are authenticated)"
        })






