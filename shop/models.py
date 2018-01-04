from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.widgets import DateInput
class Products(models.Model):
	name = models.CharField(max_length=255, default="", verbose_name='Название товара')
	desk = models.TextField(default="", verbose_name="Описание товара")
	cover = models.ImageField(upload_to='img_products/', verbose_name='Обложка товара', null=True)
	price = models.FloatField(max_length=255, default=0, verbose_name='Цена')
	hide = models.BooleanField('Скрыть?', default=False)
	
	class Meta:
		verbose_name = 'Наш товар'
		verbose_name_plural = 'Наши товары'
		ordering = ["-pk"]
	
	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Логин")
	date_of_birth = models.DateField(blank=True, null=True, verbose_name="День рождения")
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, verbose_name="Аватар пользователя")
	base_photo = models.CharField(max_length=255, default="avatar-1.png", verbose_name='Аватар по умолчанию')

	def __str__(self):
		return 'Профиль юзера {}'.format(self.user.username)
	class Meta:
		verbose_name = 'Дополнительная информация'
		verbose_name_plural = 'Дополнительная информация'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
