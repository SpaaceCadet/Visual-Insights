FROM python:3.10
 
EXPOSE 5000

WORKDIR /app

COPY . .

RUN apt-get update 
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:5000 app:server
