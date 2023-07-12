from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def save(self):
        register = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.ValidationError({"password": "Password should match"})
        register.set_password(password)
        register.save()
        return register


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    title = serializers.CharField(
        min_length=4,
        max_length=100,
        validators=[UniqueValidator(queryset=Book.objects.all())],
    )

    class Meta:
        model = Book
        fields = ["id", "title", "description", "author", "price"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Enter a valid price")
        return value
