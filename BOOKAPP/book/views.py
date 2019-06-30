from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.


def index(request):
    books = models.BookInfo.books.all()
    book_dict = {"books": books}
    return render(request, 'book_templates/base.html', book_dict)