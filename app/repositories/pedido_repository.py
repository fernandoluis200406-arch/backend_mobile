
from app.models.pedido import PedidoResposta


pedidos = []


def listar_pedidos():
    return pedidos


def adicionar_pedido(pedido: PedidoResposta):
    pedidos.append(pedido)
    return pedido
