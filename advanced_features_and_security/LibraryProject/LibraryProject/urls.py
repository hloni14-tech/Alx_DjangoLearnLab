from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('detail', views.AboutView.as_view(),
         name='detail'),
    path('admin_view', views.admin_view),
    path('librarian_view', views.librarian_view),
    path('member_view', views.member_view),
    path('add_book/', 'edit_book/', 'delete_book'),
]

from django.urls import path, include

urlpatterns = [
    # ...
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # ...
]

from django.urls import path
from relationship_app.admin import admin_site
from .views import list_books "LibraryDetailView"]

urlpatterns = [
    path('admin/', admin_site.urls),
    path('LibraryDetailView', librarydetailview.urls),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



