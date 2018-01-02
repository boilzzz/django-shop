from django.conf import settings
import os

""" Аватарки """
def files(request):
	pathToImagesFiles = os.path.join(settings.DATA_DIR, 'static/img/avatar')
	files = []
	for file in os.listdir(pathToImagesFiles):
		if file.endswith(".png"):
			files.append(file)
	return files