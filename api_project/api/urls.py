urlpatterns = [
  path('BookList.as_view'),
]

from rest_framework.routers import DefaultRouter

router.register(r'books_all', BookViewSet, basename='book_all')
