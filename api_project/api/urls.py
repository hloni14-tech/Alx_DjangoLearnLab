urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), 
]

from rest_framework.routers import DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')
