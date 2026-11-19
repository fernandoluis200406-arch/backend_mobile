
from fastapi import APIRouter

from app.models.cliente import ClienteCriacao, Cliente
from app.controllers import cliente_controller


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get(
    "/",
    response_model=list[Cliente]
)
def listar_clientes():
    return cliente_controller.listar()


@router.get(
    "/{id_cliente}",
    response_model=Cliente
)
def buscar_cliente(id_cliente: int):
    return cliente_controller.buscar(id_cliente)


@router.post(
    "/",
    response_model=Cliente,
    status_code=201
)
def criar_cliente(dados: ClienteCriacao):
    return cliente_controller.criar(dados)


@router.put(
    "/{id_cliente}",
    response_model=Cliente
)
def atualizar_cliente(id_cliente: int, dados: ClienteCriacao):
    return cliente_controller.atualizar(id_cliente, dados)


@router.delete(
    "/{id_cliente}",
    status_code=200
)
def excluir_cliente(id_cliente: int):
    return cliente_controller.excluir(id_cliente)
