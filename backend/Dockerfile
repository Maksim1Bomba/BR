FROM python:3.10-slim
WORKDIR /server
COPY app.py hello.py parser.py response.py /server
EXPOSE 8080
RUN pip install -r requirements.txt
CMD ["python": "app.py"]