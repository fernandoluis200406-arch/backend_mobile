from app.database.conexao import conectar


def listar_carros():

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT
                               id,
                               nome,
                               preco,
                               imagem,
                               descricao,
                               especificacoes
                           FROM carros
                           ORDER BY id;
                           """)

            resultados = cursor.fetchall()

            carros = []

            for registro in resultados:
                carros.append({
                    "id": registro[0],
                    "nome": registro[1],
                    "preco": float(registro[2]),
                    "imagem": registro[3],
                    "descricao": registro[4],
                    "especificacoes": registro[5]
                })

            return carros

    finally:
        conexao.close()


def buscar_carro(id_carro):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           SELECT
                               id,
                               nome,
                               preco,
                               imagem,
                               descricao,
                               especificacoes
                           FROM carros
                           WHERE id = %s;
                           """, (id_carro,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return {
                "id": registro[0],
                "nome": registro[1],
                "preco": float(registro[2]),
                "imagem": registro[3],
                "descricao": registro[4],
                "especificacoes": registro[5]
            }

    finally:
        conexao.close()


def adicionar_carro(carro):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           INSERT INTO carros (
                               nome,
                               preco,
                               imagem,
                               descricao,
                               especificacoes
                           )
                           VALUES (%s, %s, %s, %s, %s)
                               RETURNING id;
                           """, (
                               carro.nome,
                               carro.preco,
                               carro.imagem,
                               carro.descricao,
                               carro.especificacoes
                           ))

            id_gerado = cursor.fetchone()[0]

        conexao.commit()

        return buscar_carro(id_gerado)

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def atualizar_carro(id_carro, carro):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           UPDATE carros
                           SET
                               nome = %s,
                               preco = %s,
                               imagem = %s,
                               descricao = %s,
                               especificacoes = %s
                           WHERE id = %s;
                           """, (
                               carro.nome,
                               carro.preco,
                               carro.imagem,
                               carro.descricao,
                               carro.especificacoes,
                               id_carro
                           ))

            atualizado = cursor.rowcount > 0

        conexao.commit()

        if not atualizado:
            return None

        return buscar_carro(id_carro)

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()


def excluir_carro(id_carro):

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute("""
                           DELETE FROM carros
                           WHERE id = %s;
                           """, (id_carro,))

            excluido = cursor.rowcount > 0

        conexao.commit()

        return excluido

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()