from django.db import models

from django.core.validators import RegexValidator


# Create your models here.

class AdminTable(models.Model):

    Firstname = models.CharField( max_length=30)
    Lastname = models.CharField( max_length=30)
    Email = models.EmailField(max_length=50, unique=True)
    Username = models.CharField(max_length=60, unique=True)
    Password = models.CharField( max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    objects = models.Manager

    class Meta:
        db_table = "Admin_table"


class BooksTable(models.Model):
    BookName = models.CharField(max_length=200)
    AuthorOfBook = models.CharField(max_length=200)
    PublishedYear = models.CharField(max_length=200)
    objects = models.Manager


    class Meta:
        db_table = "Books_Table"
