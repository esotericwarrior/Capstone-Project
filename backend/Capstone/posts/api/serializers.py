from rest_framework import serializers
from posts.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    post_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["post", "likers", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")    # Name of month, date with a digit, year (e.g. December 25, 2019)

    def get_likes_count(self, instance):
        return instance.likers.count()

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.likers.filter(pk=request.user.pk).exists()

    def get_post_slug(self, instance):
        return instance.post.slug


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ["post_likers", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")    # Name of month, date with a digit, year (e.g. December 25, 2019)

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()

    def get_likes_count(self, instance):
        return instance.post_likers.count()

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.post_likers.filter(pk=request.user.pk).exists()
