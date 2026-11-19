
from fastapi import HTTPException

from app.models.cliente import ClienteCriacao
from app.dao import cliente_dao


def listar():
    return cliente_dao.listar_clientes()


def buscar(id_cliente: int):

    cliente = cliente_dao.buscar_cliente(id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente nao encontrado."
        )

    return cliente


def criar(dados: ClienteCriacao):

    cliente_existente = cliente_dao.buscar_por_cpf(dados.cpf)

    if cliente_existente is not None:
        raise HTTPException(
            status_code=409,
            detail="Ja existe um cliente cadastrado com esse CPF."
        )

    return cliente_dao.adicionar_cliente(dados)


def atualizar(id_cliente: int, dados: ClienteCriacao):

    cliente_existente = cliente_dao.buscar_cliente(id_cliente)

    if cliente_existente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente nao encontrado."
        )

    outro_cliente = cliente_dao.buscar_por_cpf(dados.cpf)

    if outro_cliente is not None and outro_cliente["id"] != id_cliente:
        raise HTTPException(
            status_code=409,
            detail="Esse CPF ja pertence a outro cliente."
        )

    cliente = cliente_dao.atualizar_cliente(id_cliente, dados)

    return cliente


def excluir(id_cliente: int):
    cliente = cliente_dao.buscar_cliente(id_cliente)

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente nao encontrado."
        )

    sucesso = cliente_dao.excluir_cliente(id_cliente)

    if not sucesso:
        raise HTTPException(
            status_code=409,
            detail="Nao e permitido excluir clientes que possuem pedidos registrados."
        )

    return {
        "mensagem": "Cliente removido com sucesso."
    }
