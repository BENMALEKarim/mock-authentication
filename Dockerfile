FROM python:3.11-slim 

RUN apt-get -y update && apt-get -y upgrade \
    && pip3 install flask

RUN mkdir /app 

COPY . /app

ENTRYPOINT python3 app/app.py

EXPOSE 5000