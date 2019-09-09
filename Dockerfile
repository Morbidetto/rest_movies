FROM python:3
RUN mkdir /app
WORKDIR /app
COPY requirements/base.txt /app/
RUN pip install -r base.txt
COPY ./src /app/
