from django import forms
from shop.models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('photo', 'date_of_birth','base_photo')

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Введите пароль повторно', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=30)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)