FROM python:3-alpine

LABEL authors="rmchaves"

RUN apk add --no-cache bash

WORKDIR /var/www

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["flask", "run", "--debug", "--host", "0.0.0.0"]