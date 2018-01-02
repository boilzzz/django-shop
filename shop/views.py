from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from collections import Counter
from django.db import models


from shop.forms import UserForm,ProfileForm, UserRegistrationForm
from shop.models import Products
from shop.utils import files

def home(request):
	variables = {
		'Products': Products.objects.all()
	}
	return render(request, 'index.html', variables)

""" Вход """
def sign_in(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request, 'account/sign_in_success.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/sign_in.html', {'user_form': user_form})

def logout(request):
	pass

def profile(request):
	variables = {}
	variables['files'] = files(request)
	variables['UserF'] = UserForm()
	variables['ProfileF'] = ProfileForm()
	return render(request, 'account/profile.html', variables)

def login(request):
	pass


""" Корзина """
def ajax_obj_product(request):
	if 'cart_items' not in request.session:
		request.session['cart_items'] = []
	obj_array = {}
	obj_id = Counter(request.session['cart_items'])
	print(obj_id)
	for item in obj_id:
		obj_array[item] = {}
		for i in range(1):
			obj_array[item]['product'] = Products.objects.filter(pk=item).first()
			obj_array[item]['kolv'] = obj_id[item]
			obj_array[item]['summa'] = Products.objects.filter(pk=item).first().price * obj_id[item]
	print(obj_array)
	return {
		'list': obj_array
	}

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

