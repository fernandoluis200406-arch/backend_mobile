
from fastapi import HTTPException

from app.models.carro import CarroCriacao
from app.dao import carro_dao


def listar():
    return carro_dao.listar_carros()


def buscar(id_carro: int):
    carro = carro_dao.buscar_carro(id_carro)

    if carro is None:
        raise HTTPException(
            status_code=404,
            detail="Veiculo nao encontrado."
        )

    return carro


def criar(dados: CarroCriacao):
    return carro_dao.adicionar_carro(dados)


def atualizar(id_carro: int, dados: CarroCriacao):
    carro = carro_dao.atualizar_carro(
        id_carro,
        dados
    )

    if carro is None:
        raise HTTPException(
            status_code=404,
            detail="Veiculo nao encontrado."
        )

    return carro


def excluir(id_carro: int):
    sucesso = carro_dao.excluir_carro(id_carro)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Veiculo nao encontrado."
        )

    return {
        "mensagem": "Veiculo removido com sucesso."
    }
