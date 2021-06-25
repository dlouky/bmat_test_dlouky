# pull official base image
FROM python:3.8
# set work directory
WORKDIR /bmat_test
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade cython
RUN pip install --upgrade pip
COPY ./requirements.txt /bmat_test/
RUN pip install -r requirements.txt
# copy project
COPY . /bmat_test/