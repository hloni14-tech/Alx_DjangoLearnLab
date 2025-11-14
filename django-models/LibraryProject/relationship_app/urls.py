from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('detail', views.AboutView.as_view(),
         name='detail'),
]

from django.urls import path, include

urlpatterns = [
    # ...
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # ...
]

from django.urls import path
from relationship_app.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
]
