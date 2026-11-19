
from pydantic import BaseModel


class Cliente(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str


class ClienteCriacao(BaseModel):
    nome: str
    cpf: str
    telefone: str
