from django.shortcuts import render
from rest_framework import permissions
from generics.GnericAPIView import GnericAPIView
from rest_framework.response import Response


# Create your views here.
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