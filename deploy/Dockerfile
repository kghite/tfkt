FROM python:3.8.17-slim-bullseye

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	      build-essential gcc

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /tftk

COPY deploy/requirements.txt /tftk
RUN pip install -r requirements.txt \
  && rm requirements.txt

COPY . /tftk/
