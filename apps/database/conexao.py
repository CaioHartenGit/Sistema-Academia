import psycopg

class Conectar:
    def conectar():
        conn = psycopg.connect(
            host = "localhost",
            port = 5432,
            dbname = "seudatabase",
            user = "postgres",
            password = "suasenha"
        )
        return conn