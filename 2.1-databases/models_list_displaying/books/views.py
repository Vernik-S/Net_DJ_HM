from datetime import datetime
from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')

def books_view(request):
    #template = 'books/books_list.html'
    template = 'books/books_list_my.html'
    book_objects = Book.objects.all()
    context = {
        "books" : book_objects
    }
    return render(request, template, context)

def date_view(request, date):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d' ) #
    return HttpResponse(date_time_obj)