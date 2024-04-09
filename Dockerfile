FROM ubuntu:latest
LABEL authors="rmchaves"

ENTRYPOINT ["top", "-b"]