from fastapi import APIRouter

from app.models.pedido import (
    PedidoCriacao,
    PedidoResposta
)

from app.controllers import pedido_controller


router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.post(
    "/",
    response_model=PedidoResposta,
    status_code=201
)
def criar_pedido(dados: PedidoCriacao):
    return pedido_controller.criar(dados)


@router.get(
    "/",
    response_model=list[PedidoResposta]
)
def listar_pedidos():
    return pedido_controller.listar()