from django.shortcuts import render, redirect, HttpResponse


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
