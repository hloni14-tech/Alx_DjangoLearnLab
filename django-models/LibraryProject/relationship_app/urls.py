from django.contrib import admin
from django.urls import path
from .views import list_books, "LibraryDetailView"

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('detail', views.AboutView.as_view(),
         name='detail'),
    path('views.register', 'LogoutView.as_view(template_name=',
    'LoginView.as_view(template_name'),
]

from django.urls import path, include

urlpatterns = [
    # ...
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # ...
]



