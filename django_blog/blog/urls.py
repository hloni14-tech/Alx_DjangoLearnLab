urlpatterns  [ post/<int:pk>/delete/, post/<int:pk>/update/, post/new/,
tags/<slug:tag_slug>/, PostByTagListView.as_view(),
]
