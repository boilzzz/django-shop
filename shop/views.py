from django.contrib.messages.api import error, success
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from collections import Counter
from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User

from shop.forms import UserForm, ProfileForm, UserRegistrationForm, UserLoginForm
from shop.models import Products,Profile
from shop.utils import files


def login_required(func):
	def _fn(req):
		if not req.user.is_authenticated:
			error(req, 'Для доступа к этой странице необходимо авторизоваться')
			return redirect('login')
		else:
			return func(req)

	return _fn
	
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

@login_required
def logout_view(request):
	auth.logout(request)
	return redirect('home')

def login(request):
	form = UserLoginForm(request.POST or None)
	context = { 'form': form, }
	if request.method == 'POST' and form.is_valid():
		print('yes') 
		username = form.cleaned_data.get('username', None)
		password = form.cleaned_data.get('password', None)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			print('Correct user')
		else:
			print('Wrong user')
			context['error'] = 'Логин или пароль неверный'
			return render(request, 'account/login.html', context)
		if user and user.is_active:
			auth.login(request, user)
			return redirect('home')
	return render(request, 'account/login.html', context)

@login_required
def profile(request):
	variables = {}
	variables['files'] = files(request)
	variables['UserF'] = UserForm(instance=request.user)
	variables['ProfileF'] = ProfileForm(instance=request.user.profile)
	if request.method == 'POST':
		user_form = UserForm(instance=request.user, data=request.POST)
		profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			variables['message'] = 'Удачно изменено'
			variables['files'] = files(request)
			variables['UserF'] = UserForm(instance=request.user)
			variables['ProfileF'] = ProfileForm(instance=request.user.profile)
			return render(request, 'account/profile.html', variables)
		else:
			variables['message'] = 'Ошибка'
			return render(request, 'account/profile.html', variables)
	else:
		variables['files'] = files(request)
		variables['UserF'] = UserForm(instance=request.user)
		variables['ProfileF'] = ProfileForm(instance=request.user.profile)
		return render(request, 'account/profile.html', variables)

def profile_view(request,userlogin=''):
	variables = {
		'view_user':User.objects.filter(username=userlogin)
	}
	return render(request, 'account/profile_view.html', variables)

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

