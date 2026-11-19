from app.database.conexao import conectar


def inicializar_banco():

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            # Tabela de clientes
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS clientes (
                                                                   id SERIAL PRIMARY KEY,
                                                                   nome VARCHAR(150) NOT NULL,
                               cpf VARCHAR(14) UNIQUE NOT NULL,
                               telefone VARCHAR(20) NOT NULL
                               );
                           """)

            # Tabela de carros
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS carros (
                                                                 id SERIAL PRIMARY KEY,
                                                                 nome VARCHAR(150) NOT NULL,
                               preco NUMERIC(14, 2) NOT NULL,
                               imagem TEXT NOT NULL,
                               descricao TEXT NOT NULL,
                               especificacoes TEXT[] NOT NULL DEFAULT '{}'
                               );
                           """)

            # Tabela de pedidos
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS pedidos (
                                                                  id SERIAL PRIMARY KEY,
                                                                  cliente_id INTEGER NOT NULL
                                                                  REFERENCES clientes(id),
                               total NUMERIC(14, 2) NOT NULL,
                               status VARCHAR(100) NOT NULL,
                               criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                               );
                           """)

            # Tabela de itens dos pedidos
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS itens_pedido (
                                                                       id SERIAL PRIMARY KEY,
                                                                       pedido_id INTEGER NOT NULL
                                                                       REFERENCES pedidos(id) ON DELETE CASCADE,
                               carro_id INTEGER
                               REFERENCES carros(id) ON DELETE SET NULL,
                               nome_carro VARCHAR(150) NOT NULL,
                               preco NUMERIC(14, 2) NOT NULL
                               );
                           """)

        conexao.commit()

        print("Tabelas do banco criadas/verificadas com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()