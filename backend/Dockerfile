FROM python:3.10-alpine
WORKDIR /server

COPY app.py login.py parser.py psql_config.py psql.py response.py requirements.txt /server
COPY resolv.conf /etc/resolv.conf

EXPOSE 8080

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.yandex.ru\/mirrors/g' /etc/apk/repositories
RUN apk update && apk add --no-cache gcc musl-dev python3-dev libpq-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple psycopg2-binary==2.9.3


CMD python app.py
