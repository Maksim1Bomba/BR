FROM python:3.10-slim
WORKDIR /server
COPY app.py hello.py parser.py response.py /server
EXPOSE 8080
CMD exec(open("/server/app.py").read())