FROM ubuntu:18.04

ARG AMIT_WEB_VERSION

HEALTHCHECK NONE

COPY ./requirements.txt /src/requirements.txt

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

RUN pip3 install --no-cache-dir   --trusted-host pypi.python.org -r /src/requirements.txt

# RUN pip3 install  -I\
#     Flask==1.1.2  \
#     Flask-SQLAlchemy==2.4.4 \
#     Jinja2==2.11 \
#     gunicorn==20.0.4 \
#     SQLAlchemy==1.3.23 \
#     urllib3==1.26.3 \
#     Werkzeug==1.0.1

COPY ./  /src

WORKDIR /src
