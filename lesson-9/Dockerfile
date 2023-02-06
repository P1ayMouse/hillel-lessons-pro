FROM python:3.10

ADD . /src
WORKDIR /src

RUN apt update; apt install -y gettext; rm - rf /var/apt/cache
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
