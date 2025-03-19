import psycopg2

import psql_config

class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    def start(self):
        self.conn = psycopg2.connect(
            dbname=psql_config.param['dbname'],
            user=psql_config.param['user'],
            password=psql_config.param['password'],
            host=psql_config.param['host'],
            port=psql_config.param['port'])
        self.cur = self.conn.cursor()

    def stop(self):
        self.cur.close()
        self.conn.close()

    def check_auth(self, login, password):
        self.cur.callproc("server.check_authentication", (login, password))
        ans = self.cur.fetchone()
        return ans[0]

    def add_user(self, firstname, lastname):
        self.cur.callproc("server.add_user", (firstname, lastname))
        text = self.cur.fetchone()
        print(text)
        self.conn.commit()
