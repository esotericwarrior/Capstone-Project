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

 #   @action(detail=True, methods=['post'])
 #   def post(request):
 #       form = ImageForm(request.POST, request.FILES)
  #      if form.is_valid():
            
        #url = "https://api.imgur.com/3/upload"
        #client_id = "f8a455e18a238be"
        #headers = {'Authorization': 'Client-ID ' + client_id}
        #data = {
        #        'image': self.request.FILES.get('file').read(),
        #        'title': self.request.POST['content'], 
        #        'type': 'file'
         #       }
        #response = requests.request("POST", url, headers=headers, data=data)
        #response_data = response.json()
        #upload_success = response_data['success']
        #print(response_data['data'])
        #print(upload_success)
        #external_link = response_data['data']['link']
        #serializer_class.save(url=external_link)

        #url = "https://api.imgur.com/3/upload"
        #access_token = "931ddfab9e19c9a7512147c83459ce1d457e09cf"
        #headers = {'Authorization': 'Bearer ' + access_token}
        #data = {
        #    'image': self.request.FILES.get('file').read(),
       #    'title': self.request.POST['content'], 
       #     'type': 'file'
        #    }
        #response = requests.post(url, data=data, headers=headers)
        #print(response.json())
        #response_data = response.json()
        #upload_success = response_data['success']
        #external_link = response_data['data']['link']
        #print(upload_success)



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
