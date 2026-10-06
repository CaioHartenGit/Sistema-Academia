import psycopg

class Conectar:
    def conectar():
        conn = psycopg.connect(
            host = "localhost",
            port = 5432,
            dbname = "academia",
            user = "postgres",
            password = "923252hm"
        )
        return conn