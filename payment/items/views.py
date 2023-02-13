from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Item


def paginate(request, model):
    """Разбивка вывода экземпляров модели на страницы"""
    paginator = Paginator(model, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj


def index(request):
    """"""

    template = 'index.html'
    items = Item.objects.all()
    page_obj = paginate(request, items)
    context = {
        'page_obj': page_obj
    }

    return render(request, template, context)


def success(request):

    template = 'success.html'

    return render(request, template)


def cancel(request):

    template = 'cancel.html'

    return render(request, template)
