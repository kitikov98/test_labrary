from django.urls import path
from .views import BooksView, SingleBookView, UserRegistrationView

app_name = "books"
# app_name will help us do a reverse look-up latter.


urlpatterns = [
    path('books/', BooksView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]