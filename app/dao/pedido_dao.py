
from app.database.conexao import conectar
from app.dao import item_pedido_dao


def adicionar_pedido(cliente_id, total, status, itens):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           INSERT INTO pedidos (
                               cliente_id,
                               total,
                               status
                           )
                           VALUES (%s, %s, %s)
                               RETURNING id;
                           """, (
                               cliente_id,
                               total,
                               status
                           ))

            pedido_id = cursor.fetchone()[0]

            for item in itens:
                item_pedido_dao.inserir_item(
                    cursor,
                    pedido_id,
                    item["carro_id"],
                    item["nome"],
                    item["preco"]
                )

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()

    return buscar_pedido(pedido_id)


def buscar_pedido(pedido_id):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT
                               p.id,
                               c.nome,
                               c.telefone,
                               p.total,
                               p.status
                           FROM pedidos p
                                    INNER JOIN clientes c
                                               ON c.id = p.cliente_id
                           WHERE p.id = %s;
                           """, (pedido_id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            pedido = {
                "id": registro[0],
                "nome_cliente": registro[1],
                "telefone": registro[2],
                "total": float(registro[3]),
                "status": registro[4],
                "itens": item_pedido_dao.listar_itens_por_pedido(
                    pedido_id
                )
            }

            return pedido

    finally:
        conexao.close()


def listar_pedidos():

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT
                               p.id,
                               c.nome,
                               c.telefone,
                               p.total,
                               p.status
                           FROM pedidos p
                                    INNER JOIN clientes c
                                               ON c.id = p.cliente_id
                           ORDER BY p.id;
                           """)

            resultados = cursor.fetchall()

            pedidos = []

            for registro in resultados:

                pedido_id = registro[0]

                pedido = {
                    "id": pedido_id,
                    "nome_cliente": registro[1],
                    "telefone": registro[2],
                    "total": float(registro[3]),
                    "status": registro[4],
                    "itens": item_pedido_dao.listar_itens_por_pedido(
                        pedido_id
                    )
                }

                pedidos.append(pedido)

            return pedidos

    finally:
        conexao.close()
