from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("book_list", views.PublicView.as_view(), name="book_list"),
    path("books", views.BookCreate.as_view(), name="book_list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
]
