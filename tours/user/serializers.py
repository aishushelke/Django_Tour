from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import user


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["fname", "lname", "password", "username", "email",  "contact"]

    def create(self, validated_data):
        users = user.objects.create_user(
            fname=validated_data.pop('fname'),
            lname=validated_data.pop('lname'),
            username=validated_data.pop('username'),
            password=validated_data.pop('password'),
            email=validated_data.pop('email'),
            contact=validated_data.pop('contact'),

        )
        return users

class UserLoginSerializer(serializers.Serializer):
        email = serializers.CharField(required=True)
        password = serializers.CharField(required=True)

        def validate(self, attrs):
            self.users = authenticate(username=attrs.pop("email"), password=attrs.pop("password"))
            if self.users:
                return attrs
            else:
                raise serializers.ValidationError()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["id", "fname", "lname", "email","contact"]