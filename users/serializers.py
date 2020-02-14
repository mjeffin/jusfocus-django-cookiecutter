from rest_framework import serializers
from .models import User
import json

class CurrentUserSerializer(serializers.ModelSerializer):
    """The custom serializer which is the end point fot auth/me"""
    
    class Meta:
        model = User
        exclude = ['password']

class UserCreateSerializer(serializers.ModelSerializer):
    """The custom serializer to craete user    
    
    https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
    https://stackoverflow.com/questions/22924122/using-user-objects-get-or-create-gives-invalid-password-format-in-django
    Adds the created user to hubspot.
    Exception will be raised if there was error in adding to hubspot.
    """
    
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'password')
    
    def create(self, validated_data):
        """Nested serializer need to over-ride the create fn to work"""
        user = User.objects.create( **validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user

