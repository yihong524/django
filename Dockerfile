FROM python:3.7-alpine
WORKDIR /src/app

COPY . /src/app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]