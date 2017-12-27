from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Products
from django.core import serializers
from collections import Counter
def home(request):
	variables = {
		'Products': Products.objects.all()
	}
	return render(request, 'index.html', variables)

def add_to_cart(request):
		id = request.GET.get('id', False)
		product = Products.objects.filter(pk=id)
		if id and product.exists():	
			request.session['cart_items'].append(id)
			request.session.modified = True
			product__price_json = serializers.serialize("json",product)
			return HttpResponse(product__price_json)
		else:
			return HttpResponse('error')

def view_cart(request):
	variables = ajax_obj_product(request)
	if request.is_ajax():
		clear_cart = request.GET.get('clear_cart', False)
		if clear_cart:	
			del request.session['cart_items']
			return render(request, 'cart.html', ajax_obj_product(request))
	return render(request, 'cart.html', variables)

def ajax_obj_product(request):
	if 'cart_items' not in request.session:
		request.session['cart_items'] = []
	obj_array = {}
	obj_id = Counter(request.session['cart_items'])
	print(obj_id)
	"""obj_id[item] количество, item - id товара"""
	b = 1
	for item in obj_id:
		obj_array[item] = {}
		for i in range(b):
			obj_array[item]['product'] = Products.objects.filter(pk=item).first()
			obj_array[item]['kolv'] = obj_id[item]
			obj_array[item]['summa'] = Products.objects.filter(pk=item).first().price * obj_id[item]
	print(obj_array)
	return {
		'list': obj_array
	}

