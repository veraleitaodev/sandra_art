from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the redirect page to redirect the user """

    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get({})

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
