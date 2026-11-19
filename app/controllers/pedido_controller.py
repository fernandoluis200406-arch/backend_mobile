
from fastapi import HTTPException

from app.models.pedido import PedidoCriacao
from app.models.cliente import ClienteCriacao

from app.dao import (
    carro_dao,
    cliente_dao,
    pedido_dao
)


def criar(dados: PedidoCriacao):

    itens = []
    total = 0.0

    # Verifica se todos os veículos existem.
    for id_carro in dados.carros_ids:

        carro = carro_dao.buscar_carro(id_carro)

        if carro is None:
            raise HTTPException(
                status_code=404,
                detail=f"Veiculo {id_carro} nao encontrado."
            )

        item = {
            "carro_id": carro["id"],
            "nome": carro["nome"],
            "preco": carro["preco"]
        }

        itens.append(item)
        total += carro["preco"]

    # Procura o cliente pelo CPF.
    cliente = cliente_dao.buscar_por_cpf(dados.cpf)

    # Cadastra o cliente caso ainda nao exista.
    if cliente is None:

        novo_cliente = ClienteCriacao(
            nome=dados.nome_cliente,
            cpf=dados.cpf,
            telefone=dados.telefone
        )

        cliente = cliente_dao.adicionar_cliente(
            novo_cliente
        )

    # Cria o pedido no banco de dados.
    pedido = pedido_dao.adicionar_pedido(
        cliente_id=cliente["id"],
        total=round(total, 2),
        status="Solicitacao recebida",
        itens=itens
    )

    return pedido


def listar():

    return pedido_dao.listar_pedidos()
