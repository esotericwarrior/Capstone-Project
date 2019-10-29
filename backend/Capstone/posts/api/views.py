from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from posts.api.permissions import IsAuthorOrReadOnly
from posts.api.serializers import CommentSerializer, PostSerializer
from posts.models import Comment, Post

class PostViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Post."""
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

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
        if post.comments.filter(author=request_user).exists():
            raise ValidationError("You have already commented on this post!")

        serializer.save(author=request_user, post=post)
