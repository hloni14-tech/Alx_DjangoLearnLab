from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('register/', include('user_registration.urls'))
    path('login/', include('user_authentication.urls')),
    path('post_views/', include('post_views.urls')),
    path('comments/', include('comments.urls'),)
    path('feed/')
    path('<int:pk>/like/'), 
    path('<int:pk>/unlike/'),
]

from django.urls import path
from social_media_api.social_media_api import admin_site

urlpatterns = [
    path('admin/ , admin_site.urls'),
]
