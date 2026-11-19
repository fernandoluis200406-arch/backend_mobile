
from app.database.conexao import conectar


def adicionar_item(pedido_id, carro_id, nome_carro, preco):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           INSERT INTO itens_pedido (
                               pedido_id,
                               carro_id,
                               nome_carro,
                               preco
                           )
                           VALUES (%s, %s, %s, %s)
                               RETURNING id;
                           """, (
                               pedido_id,
                               carro_id,
                               nome_carro,
                               preco
                           ))

            id_gerado = cursor.fetchone()[0]

        conexao.commit()

        return id_gerado

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def listar_itens_por_pedido(pedido_id):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT
                               carro_id,
                               nome_carro,
                               preco
                           FROM itens_pedido
                           WHERE pedido_id = %s
                           ORDER BY id;
                           """, (pedido_id,))

            resultados = cursor.fetchall()

            return [
                {
                    "carro_id": registro[0],
                    "nome": registro[1],
                    "preco": float(registro[2])
                }
                for registro in resultados
            ]

    finally:
        conexao.close()


def inserir_item(cursor, pedido_id, carro_id, nome_carro, preco):

    cursor.execute("""
                   INSERT INTO itens_pedido (
                       pedido_id,
                       carro_id,
                       nome_carro,
                       preco
                   )
                   VALUES (%s, %s, %s, %s);
                   """, (
                       pedido_id,
                       carro_id,
                       nome_carro,
                       preco
                   ))
