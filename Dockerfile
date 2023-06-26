FROM python:3.11-alpine

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN apk add build-base libffi-dev

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY . .