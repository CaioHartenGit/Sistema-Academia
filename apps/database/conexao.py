import psycopg

class Conectar:
    def conectar():
        conn = psycopg.connect(
            host = "localhost",
            port = 5432,
            dbname = "seudb",
            user = "postgres",
            password = "suasenha"
        )
        return conn