from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import django
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField(null=True)
    mrp = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} by {self.author}'


class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(
        null=True, blank=True)
    # 1 means available for issue, 0 means not
    status = models.BooleanField(default=False)
    borrower = models.ForeignKey(
        User, related_name='borrower', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.book.title} , {str(self.borrow_date)}'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        User,  null=True,  on_delete=models.SET_NULL)
    rating = models.FloatField()

    def __str__(self):
        return f'{self.book.title} , {self.reviewer} , {self.rating} '
