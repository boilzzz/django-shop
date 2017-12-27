from django.db import models

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
        