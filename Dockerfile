# FROM python:3.7

# RUN pip3 install git+https://github.com/channelcat/sanic

# COPY requirements.txt /requirements.txt
# RUN pip3 install -r requirements.txt

# ADD . /app
# COPY python-sanic-mongodb-sample-app /app




# EXPOSE 8000

# WORKDIR /app
# CMD ["python3", "main.py"] 


FROM python:3.7-slim-stretch
RUN apt-get update && apt-get -y install gcc
RUN apt-get -y install virtualenv
RUN pip3 install sanic_limiter
RUN pip3 install sanic-mongodb-extension

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
ADD . /app
COPY python-sanic-mongodb-sample-app /app
EXPOSE 8000
WORKDIR /app
# WORKDIR /python-sanic-mongodb-sample-app
# RUN virtualenv venv
# RUN . venv/bin/activate
# RUN pip3 install -r requirements.txt
# RUN python3 main.py
RUN "ls"
CMD ["python3", "main.py"] 