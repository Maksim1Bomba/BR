FROM python:3.10-slim
WORKDIR /server
COPY app.py login.py parser.py psql_config.py psql.py response.py requirements.txt /server
EXPOSE 8080
RUN pip install -r requirements.txt
CMD python app.py