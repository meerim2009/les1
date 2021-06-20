from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from test_app.models import Post, Comment
from test_app.serializers import PostsSerializers, CommentSerializer


@api_view(["GET"])
def get_posts(request):
    posts = Post.objects.all()
    print(posts)
    serializer = PostsSerializers(posts, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_post(request, id):
    post = Post.objects.filter(id=id).first()
    serializer = PostsSerializers(post).data
    return Response(data=serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_comment(request, id):
    comments = Comment.objects.filter(post_id=id)
    serializer = CommentSerializer(comments, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


