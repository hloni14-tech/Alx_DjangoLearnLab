from django.shortcuts import render
from app.notifications.models import Notifications
from app.notifications.views import LikePostView

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
from dd.django_blog.blog.models import Post

class SampleGenericView(GnericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a sample generic view response."})
    
    def get_following(request):
        return following.all()
    
    def get_post_objects(request):
        return Post.objects.all.filter()

    def get_posts(request, following_users): 
        return Post.objects.filter(author__in=following_users).order_by()

class LikePostView(GnericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        return Response({"message": f"Post {post_id} liked."})
    
class UnlikePostView(GnericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        return Response({"message": f"Post {post_id} unliked."})

class NotificationListView(GnericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "List of notifications."})

def get_object(self.pk):
    return generics.get_object_or_404(Post, pk=pk) 
    
def get_like_object(request, post):
    return Like.objects.get_or_create(user=request.user, post=post)
    
def create_notification(request, recipient, actor, verb, post=None):
    return Notification.objects.create
    



 


















