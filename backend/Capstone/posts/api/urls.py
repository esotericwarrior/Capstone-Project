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
]
