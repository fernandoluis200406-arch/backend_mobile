
from fastapi import APIRouter

from app.models.carro import Carro, CarroCriacao
from app.controllers import carro_controller


router = APIRouter(
    prefix="/carros",
    tags=["Carros"]
)


@router.get("/", response_model=list[Carro])
def listar_carros():
    return carro_controller.listar()


@router.get("/{id_carro}", response_model=Carro)
def buscar_carro(id_carro: int):
    return carro_controller.buscar(id_carro)


@router.post("/", response_model=Carro, status_code=201)
def criar_carro(dados: CarroCriacao):
    return carro_controller.criar(dados)


@router.put("/{id_carro}", response_model=Carro)
def atualizar_carro(id_carro: int, dados: CarroCriacao):
    return carro_controller.atualizar(id_carro, dados)


@router.delete("/{id_carro}")
def excluir_carro(id_carro: int):
    return carro_controller.excluir(id_carro)
