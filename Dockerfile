FROM python:3.7-slim-stretch
RUN apt-get update && apt-get -y install gcc
RUN apt-get -y install virtualenv
RUN pip3 install sanic_limiter
RUN pip3 install sanic-mongodb-extension

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 8082     
WORKDIR /app
CMD ["python3", "main.py"] 