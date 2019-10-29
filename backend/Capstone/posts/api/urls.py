from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api import views as pv

router = DefaultRouter()
router.register(r"posts", pv.PostViewSet) # Posts endpoint

urlpatterns = [
    path("", include(router.urls)),

    # Path to view all comments of specific post.
    path("posts/<slug:slug>/comments/", # /posts/slug+randomly_generated_string/comments/
         pv.CommentListAPIView.as_view(),
         name="comment-list"),

    # Path to comment on a specific post.
    path("posts/<slug:slug>/comment/",  # /posts/slug+randomly_generated_string/comment/
         pv.CommentCreateAPIView.as_view(),
         name="comment-create"),

    # Path to view a specific comment.
    path("comments/<int:pk>/",  # /comments/integer-primarykey/
         pv.CommentRUDAPIView.as_view(),
         name="comment-detail"),

    # Path to like a specific comment.
    path("comments/<int:pk>/like/", # /comments/integer-primarykey/like/
         pv.CommentLikeAPIView.as_view(),
         name="comment-like")
]
