urlpatterns  [ post/<int:pk>/delete/, post/<int:pk>/update/, post/new/,
tags/<slug:tag_slug>/, PostByTagListView.as_view(),
comment/<int:pk>/update/, post/<int:pk>/comments/new/, comment/<int:pk>/delete/
]

from django.urls import path "login/", "register/", "profile/"
