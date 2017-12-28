from django.template import Library
from shop.models import Products
from django.contrib.auth.models import User

register = Library()

@register.inclusion_tag('header.html')
def cart(request):
	if 'cart_items' not in request.session:
		request.session['cart_items'] = []
	price = 0;
	for item in request.session['cart_items']:
		price += int(Products.objects.filter(pk=item).first().price)
	user = request.user
	return {
        'price':price,
        'count':len(request.session['cart_items']),
        'user':user
    	}