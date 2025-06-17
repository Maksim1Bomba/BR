import os

param = dict(
    dbname='database_name',
    user='user_name',
    password=os.environ["PSQL_PASSWORD"],
    host='postgres',
    port='5432'
)

