from .models import Book
from .serializers import BooksSerializer, UserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .tasks import send_welcome_email


class BooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_email = response.data.get('email')
        send_welcome_email.delay(user_email)
        return response
