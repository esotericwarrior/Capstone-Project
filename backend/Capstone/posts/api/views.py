from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser

from posts.api.permissions import IsAuthorOrReadOnly
from posts.api.serializers import CommentSerializer, PostSerializer
from posts.models import Comment, Post
from iv.forms import VideoForm, ImageForm
from rest_framework.decorators import action
import requests
import json


class CommentLikeAPIView(APIView):
    """Allow users to add/remove a like to/from a Comment instance."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):  # Unlike
        """Remove request.user from the 'likers' queryset of a Comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.likers.remove(user) # Remove user's like from instance
        comment.save()  # Save the instance

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):    # Like
        """Add request.user to the 'likers' queryset of a Comment instance."""
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.likers.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostLikeAPIView(APIView):
    """Allow users to add/remove a like to/from a Post instance."""
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):  # Unlike
        """Remove request.user from the 'likers' queryset of a Post instance."""
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        post.post_likers.remove(user) # Remove user's like from instance
        post.save()  # Save the instance

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):    # Like
        """Add request.user to the 'likers' queryset of a Post instance."""
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        post.post_likers.add(user)
        post.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(post, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for a Comment instance to its author."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Post."""
    queryset = Post.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    parser_classes = (FormParser, MultiPartParser, FileUploadParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class CommentCreateAPIView(generics.CreateAPIView):
    """Allow users to Comment a Post instance if they haven't already."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        post = get_object_or_404(Post, slug=kwarg_slug)

        # Raises a validation error if the user has already commented.
        # if post.comments.filter(author=request_user).exists():
        #     raise ValidationError("You have already commented on this post!")

        serializer.save(author=request_user, post=post)

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(post__slug=kwarg_slug).order_by("-created_at")
