import os

param = dict(
    dbname='a1337',
    user='a1337',
    password=os.environ["PSQL_PASSWORD"],
    host='localhost',
    port='5432'
)

