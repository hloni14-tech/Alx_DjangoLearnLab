from rest_framework import generics
from .models import Book, MyModel
from .serializers import BookSerializer, MyModelSerializer
from rest_framework import .viewsets.ModelViewSet

class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSetModelViewSet(generics.ModelViewSet):
    



