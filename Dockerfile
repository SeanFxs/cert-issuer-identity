# from https://github.com/Kalimaha/simple_flask_dockerizer
FROM ubuntu:14.04
MAINTAINER Kim Duffy "kimhd@mit.edu"

RUN apt-get update

# Install Python.
RUN apt-get install -y -q build-essential python-gdal python-simplejson
RUN apt-get install -y python python-pip wget
RUN apt-get install -y python-dev

# Create a working directory.
RUN mkdir cert-issuer-identity

# Install VirtualEnv.
RUN pip install virtualenv

# Add requirements file.
ADD requirements.txt /cert-issuer-identity/requirements.txt

# Add the script that will start everything.
#ADD /cert-issuer-identity/app.py /cert-issuer-identity/app.py
ADD run.py /cert-issuer-identity/run.py

# Run VirtualEnv.
RUN virtualenv /cert-issuer-identity/env/
RUN /cert-issuer-identity/env/bin/pip install wheel

RUN /cert-issuer-identity/env/bin/pip install -r /cert-issuer-identity/requirements.txt

COPY . /cert-issuer-identity

RUN pip install /cert-issuer-identity
