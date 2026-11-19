
from pydantic import BaseModel


class Carro(BaseModel):
    id: int
    nome: str
    preco: float
    imagem: str
    descricao: str
    especificacoes: list[str]


class CarroCriacao(BaseModel):
    nome: str
    preco: float
    imagem: str
    descricao: str
    especificacoes: list[str]
