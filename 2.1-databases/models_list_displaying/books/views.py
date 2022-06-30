from datetime import datetime
from http.client import HTTPResponse

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list_my.html'
    book_objects = Book.objects.all()
    context = {
        "books" : book_objects
    }
    return render(request, template, context)

def date_view(request, date):
    template = 'books/date.html'
    #date_time_obj = datetime.strptime(date, '%Y-%m-%d' ).date()
    book_objects = Book.objects.all()

    all_dates = [b.pub_date for b in book_objects]
    all_dates = list(set(all_dates)) #remove duplicates
    all_dates.sort()
    all_date_string = [datetime.strftime(date, '%Y-%m-%d' ) for date in all_dates]





    paginator = Paginator(all_date_string, 1)
    current_page_num = all_date_string.index(date) + 1
    page = paginator.get_page(current_page_num)

    book_objects = Book.objects.filter(pub_date=date)

    context = {
        "books" : book_objects,
        "page": page,
    }
    return render(request, template, context)