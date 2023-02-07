FROM python:3.10

ADD requirements.txt /requirements.txt
RUN apt update; apt install -y gettext; rm -rf /var/apt/cache
RUN pip install -r /requirements.txt

ADD . /src
WORKDIR /src


CMD pip install -r requirements.txt && invoke runit
