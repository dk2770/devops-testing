FROM ubuntu

MAINTAINER "kumar207"

USER root

RUN apt-get update

RUN apt-get install -y wget

RUN apt-get install -y python3.7

RUN apt install -y python3-pip

RUN pip3 install flask

RUN apt-get update

COPY . /app

WORKDIR /app

EXPOSE 5001

ENTRYPOINT ["python3"]

CMD ["testing.py"]
