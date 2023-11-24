from rest_framework import serializers
from .models import Book, CustomUser


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'year', 'isbn')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'date_joined')