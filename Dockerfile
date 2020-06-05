# ========================================================
# Python/djangoの実行環境構築
# ========================================================
FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN pip install --upgrade pip

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code
