import os

import psycopg
from dotenv import load_dotenv


# Carregar variáveis do arquivo .env
load_dotenv()


# Dados de conexão
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Estabelecer conexão com PostgreSQL
def conectar():

    configuracoes = {
        "DB_HOST": DB_HOST,
        "DB_PORT": DB_PORT,
        "DB_NAME": DB_NAME,
        "DB_USER": DB_USER,
        "DB_PASSWORD": DB_PASSWORD
    }

    for chave, valor in configuracoes.items():
        if not valor:
            raise ValueError(
                f"Configuração ausente no arquivo .env: {chave}"
            )

    conexao = psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    return conexao