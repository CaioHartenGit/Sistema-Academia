import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class Conectar:

    def conectar():
        conn = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "5432")),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        return conn