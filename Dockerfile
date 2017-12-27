FROM python:3-onbuild
WORKDIR /usr/src/app
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]