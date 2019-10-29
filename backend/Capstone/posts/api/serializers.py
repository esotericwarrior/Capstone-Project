from rest_framework import serializers
from posts.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    post_slug = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["post", "likers", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")    # Name of month, date with a digit, year (e.g. December 25, 2019)

    def get_likes_count(self, instance):
        return instance.likers.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.likers.filter(pk=request.user.pk).exists()

    def get_post_slug(self, instance):
        return instance.post.slug
