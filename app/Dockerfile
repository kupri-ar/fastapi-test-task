# pull the official docker image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

RUN apk add --no-cache netcat-openbsd \
    postgresql-dev \
    gcc \
#    python3-dev \
    libffi-dev \
    musl-dev \
    jpeg-dev \
    libwebp-dev \
    libzip-dev \
    libsodium libsodium-dev \
    make \
    build-base

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .