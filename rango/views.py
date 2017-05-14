from django.shortcuts import render
from .models import Category, Page


def index(request):
    category_likes = Category.objects.order_by("-likes")[:5]
    view_pages = Page.objects.order_by("-views")[:5]
    context_dict = {
        'liked_categories': category_likes,
        'viewed_pages': view_pages,
    }
    return render(request, "rango/index.html", context_dict)


def about(request):
    context_dict = {'my_name':"Aishwarya Pradhan"}
    return render(request, "rango/about.html", context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, "rango/category.html", context_dict)