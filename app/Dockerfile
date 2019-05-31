FROM python:3.7-alpine
WORKDIR /src/app

COPY . /src/app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "web_project.wsgi:application"]