# pull official base image
FROM python:3.8
# set work directory
WORKDIR /bmat_test_dlouky
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade cython
COPY ./requirements.txt /bmat_test_dlouky/
RUN pip install -r requirements.txt
# copy project
COPY . /bmat_test_dlouky/