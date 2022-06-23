from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get("sort", "name")




    phones_objects = list(Phone.objects.all())

    if sort_type == "min_price":
        phones_objects.sort(key=lambda ph: ph.price)
    elif sort_type == "max_price":
        phones_objects.sort(key=lambda ph: ph.price, reverse=True)
    else: #default by name
        phones_objects.sort(key=lambda ph: ph.name)



    context = {
        "phones":phones_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug = slug)
    context = {
        "phone" : phone
    }
    return render(request, template, context)
