FROM python:3.9.16-slim-bullseye as builder

MAINTAINER master

COPY . .

WORKDIR /

RUN python -m pip install --upgrade pip

RUN pip install -r  requiremnts.txt

EXPOSE 31051

CMD ["python","TCPListener.py"]
