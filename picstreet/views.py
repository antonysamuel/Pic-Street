from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Image, Category


def show_about_page(request):
    return render(request, 'about.html', {})


def show_home_page(request):
    images = Image.objects.all()
    cat = Category.objects.all()
    data = {
        'images': images,
        'cat': cat
    }
    return render(request, 'home.html', data)


def show_category_page(request, cid):

    category = Category.objects.get(pk=cid)

    cat = Category.objects.all()

    images = Image.objects.filter(cat=category)

    data = {
        'images': images,
        'cat': cat
    }
    return render(request, 'home.html', data)
