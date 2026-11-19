from pydantic import BaseModel, Field


class PedidoCriacao(BaseModel):
    nome_cliente: str
    cpf: str
    telefone: str
    carros_ids: list[int] = Field(min_length=1)


class ItemPedido(BaseModel):
    carro_id: int | None
    nome: str
    preco: float


class PedidoResposta(BaseModel):
    id: int
    nome_cliente: str
    telefone: str
    itens: list[ItemPedido]
    total: float
    status: str