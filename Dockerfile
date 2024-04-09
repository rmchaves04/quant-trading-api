FROM python:3-alpine

LABEL authors="rmchaves"

RUN apk add --no-cache bash

COPY . /var/www

WORKDIR /var/www

RUN pip install -r ./requirements.txt

CMD ["python", "api/main.py"]