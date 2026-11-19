
from app.database.conexao import conectar


def listar_clientes():

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT id, nome, cpf, telefone
                           FROM clientes
                           ORDER BY id;
                           """)

            resultados = cursor.fetchall()

            return [
                {
                    "id": registro[0],
                    "nome": registro[1],
                    "cpf": registro[2],
                    "telefone": registro[3]
                }
                for registro in resultados
            ]

    finally:
        conexao.close()


def buscar_cliente(id_cliente):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT id, nome, cpf, telefone
                           FROM clientes
                           WHERE id = %s;
                           """, (id_cliente,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return {
                "id": registro[0],
                "nome": registro[1],
                "cpf": registro[2],
                "telefone": registro[3]
            }

    finally:
        conexao.close()


def buscar_por_cpf(cpf):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT id, nome, cpf, telefone
                           FROM clientes
                           WHERE cpf = %s;
                           """, (cpf,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return {
                "id": registro[0],
                "nome": registro[1],
                "cpf": registro[2],
                "telefone": registro[3]
            }

    finally:
        conexao.close()


def adicionar_cliente(cliente):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           INSERT INTO clientes (
                               nome,
                               cpf,
                               telefone
                           )
                           VALUES (%s, %s, %s)
                               RETURNING id;
                           """, (
                               cliente.nome,
                               cliente.cpf,
                               cliente.telefone
                           ))

            id_gerado = cursor.fetchone()[0]

        conexao.commit()

        return buscar_cliente(id_gerado)

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def atualizar_cliente(id_cliente, cliente):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           UPDATE clientes
                           SET
                               nome = %s,
                               cpf = %s,
                               telefone = %s
                           WHERE id = %s;
                           """, (
                               cliente.nome,
                               cliente.cpf,
                               cliente.telefone,
                               id_cliente
                           ))

            atualizado = cursor.rowcount > 0

        conexao.commit()

        if not atualizado:
            return None

        return buscar_cliente(id_cliente)

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()

def excluir_cliente(id_cliente):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT COUNT(*)
                           FROM pedidos
                           WHERE cliente_id = %s;
                           """, (id_cliente,))

            quantidade_pedidos = cursor.fetchone()[0]

            if quantidade_pedidos > 0:
                return False

            cursor.execute("""
                           DELETE FROM clientes
                           WHERE id = %s;
                           """, (id_cliente,))

            excluido = cursor.rowcount > 0

        conexao.commit()

        return excluido

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()