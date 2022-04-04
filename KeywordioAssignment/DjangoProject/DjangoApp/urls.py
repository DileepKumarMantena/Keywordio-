from django.urls import path

from .views import *

urlpatterns = [
    path('AdminRegister/', AdminRegistrationApi.as_view(), name="Register An Admin"),
    path('AdminLogin/', AdminLoginApi.as_view(), name="Login Of The Admin"),
    path("BooksEntryApi/", BooksEntryApi.as_view(), name="Books Entry Table"),
    path('GetEnterdBooks/', GetEnterdBooks.as_view(), name=" Get All Entered Books"),
    path('BooksUpdate/<int:id>/', BooksUpdate.as_view(), name="Update Books"),
    path('DeleteBook/<int:id>/',DeleteBook.as_view(),name="Delete Books")
]
