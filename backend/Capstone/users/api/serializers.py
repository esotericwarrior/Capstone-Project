from rest_framework import serializers
from users.models import CustomUser

# This endpoint provides the username of user that is currently connected to the application
class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]
