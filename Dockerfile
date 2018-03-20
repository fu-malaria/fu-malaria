FROM python:latest

MAINTAINER InnovativeInventor

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y && apt-get install git nginx -y
RUN git clone https://github.com/InnovativeInventor/fu-malaria /usr/src/app
RUN pip3 install gunicorn flask numpy opencv-python

WORKDIR /usr/src/app/flask

EXPOSE 8000
CMD [ "gunicorn", "app:app", "-w", "4", "--bind", ":8000" ]
