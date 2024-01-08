FROM alpine:3.19.0

WORKDIR /app

RUN set -xe;

COPY . .
COPY requirements.txt .

RUN apk add --update alpine-sdk;
RUN apk add --no-cache python3 py3-pip tini build-base python3-dev gcc gfortran musl-dev;
RUN pip install --break-system-packages -r requirements.txt;
RUN python3 manage.py makemigrations;
RUN python3 manage.py migrate;
RUN addgroup -g 1000 appuser;
RUN adduser -u 1000 -G appuser -D -h /app appuser;
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000/tcp
ENTRYPOINT ["tini", "--"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
