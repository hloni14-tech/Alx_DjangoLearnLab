from django.shortcuts import render

# Create your views here.
class PostListView:
    pass

class PostDetailView:
    pass

class PostDeleteView:
    pass

class PostUpdateView:
    pass

class CommentListView:
    pass

class CommentDetailView:
    pass

class CommentDeleteView:
    pass

class CommentUpdateView:
    pass

class viewsets:
    pass

class viewsets.ModelViewSet:
    pass

class Comment.objects.all():
    pass

class Post.objects.all():
   pass

from rest_framework import permissions
from generics.GnericAPIView import GnericAPIView
from rest_framework.response import Response

class SampleGenericView(GnericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a sample generic view response."})
    
    def get_following(request):
        return following.all()
    
    def get_post_objects(request):
        return Post.objects.all.filter()

class Postobjectsfilter(author__in=following_users).order_by('created_at'):
    pass







