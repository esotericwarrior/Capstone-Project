from django.db import models
from django.conf import settings    # Import Custom User Class from settings.py

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="posts")
    post_likers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="post_likes")
    file = models.FileField(null=True, max_length=255)

    def __str__(self):
        return self.content


class Comment(models.Model):    # Post Comment
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        body = models.TextField()
        post = models.ForeignKey(Post,  # There can't be a comment without a post
                                on_delete=models.CASCADE,
                                related_name="comments")
        author = models.ForeignKey(settings.AUTH_USER_MODEL,    # Each comment has an author
                                    on_delete=models.CASCADE)
        likers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="likes")

        def __str__(self):
            return self.author.username
