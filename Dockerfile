FROM python:3.12.7-alpine

RUN apk update && \
    apk add --virtual --no-cache  --virtual .build-deps \
    gcc musl-dev postgresql-dev && \
    apk del gcc musl-dev .build-deps && \
    apk add git gettext && \
    pip install --upgrade pip && \
    rm -f /var/cache/apk/*

WORKDIR /app

COPY ./src/api/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD ["gunicorn", "--worker-tmp-dir",  "/dev/shm", "--bind", ":8000", "core.wsgi:application"]
