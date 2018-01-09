FROM python:2.7-alpine3.7

RUN mkdir -p /webapp/
WORKDIR /webapp

COPY . /webapp/

RUN pip install -r requirements.txt

EXPOSE 5000

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
