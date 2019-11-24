from rest_framework import serializers
from iv.models import Image, Video

class ImageSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    description = serializers.SerializerMethodField()
    #created_at = serializers.SerializerMethodField()
    #slug = serializers.SlugField(read_only=True)
    #comments_count = serializers.SerializerMethodField()
    #user_has_commented = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = '__all__'
    
    def get_description(self, instance):
        return instance.description    # Name of month, date with a digit, year (e.g. December 25, 2019)

