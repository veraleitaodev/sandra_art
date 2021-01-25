from django.shortcuts import render
from products.models import Collection, Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    collection = Collection.objects.all()
    products_carousel = Product.objects.all().order_by('id')[:4]
    context = {
        'products_carousel': products_carousel,
        'collection': collection,
    }

    return render(request, 'home/index.html', context)
