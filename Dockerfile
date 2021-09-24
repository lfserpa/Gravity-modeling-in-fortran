FROM python:3.9.7-alpine3.14

RUN apt update &&\
    apt install build-essential