from django.conf import settings
from django import template

register = template.Library()

@register.filter()
def static_url(value,arg):
	return ''.join(["http://", settings.SITE_URL, settings.STATIC_URL,arg, value])