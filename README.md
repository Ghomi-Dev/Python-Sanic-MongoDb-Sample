# Python Sanic MongoDb Sample



#### This project is created as a sample :

* Python 3
* Sanic Framework
* Sanic-Motor
* MongoDb
* Sanic-Limit
* Sanic-Jinja2
* Docker
* Docker-Composer



#### Functionalities :

* Simple CRUD Functions based on Mongodb
* Requests limit per user: 5 requests per minute
* Dockerized web app



##### you can use docker-composer to use this repo hassle free



#### Using Docker-Composer:

- Clone it and use commands below in terminal

- **to build:**

  sudo docker-compose -f docker-compose.dev.yml up -d --build

- **to run:**

  sudo docker-compose -f docker-compose.dev.yml up 



#### Running with python 3:

* **use commands below in terminal:**
  * pip3 intall -r requirements.txt
  * paython3 myapp.py

**after running web app , it can be browsed at http://0.0.0.0:8082/**

**Feel free to fork and enhance this experience**