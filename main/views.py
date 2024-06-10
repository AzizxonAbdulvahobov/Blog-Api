from rest_framework.permissions import  IsAuthenticated, IsAuthenticatedOrReadOnly
from . import serializers
from rest_framework import viewsets
from . import models

class BlogApiViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class LikeApiViewSet(viewsets.ModelViewSet):
    queryset = models.Like.objects.all()
    serializer_class = serializers.LikeSerializer


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer