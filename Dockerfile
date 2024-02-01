FROM python:3.11-slim 

RUN pip3 install flask

RUN mkdir /app 

COPY . /app

ENTRYPOINT python3 app/app.py

EXPOSE 5000