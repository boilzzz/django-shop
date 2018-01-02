from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from . import models
from shop.utils import files

@admin.register(models.Products)
class Products(admin.ModelAdmin):
	pass

class Profile_custom(admin.StackedInline):
	model = models.Profile
	template = 'admin/stacked.html'

# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
	inlines = (Profile_custom, )
	def change_view(self, request, object_id, form_url='', extra_context=None):
		context = {}
		context.update(extra_context or {})
		context.update({'files':files(request),'default_name':models.Profile.objects.filter(pk=object_id).first()})
		return self.changeform_view(request, object_id, form_url, context)

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)