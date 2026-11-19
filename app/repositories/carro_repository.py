
from app.models.carro import Carro, CarroCriacao


carros = [
    Carro(
        id=1,
        nome="Audi R8 V10 Performance",
        preco=1310990.00,
        imagem="assets/carro2.jpg",
        descricao=(
            "O Audi R8 V10 Performance quattro possui "
            "motor V10 5.2 FSI aspirado, alto desempenho "
            "e tracao integral quattro."
        ),
        especificacoes=[
            "Motor: V10 5.2 FSI",
            "Potencia: 620 cv",
            "Torque: 580 Nm",
            "Tracao: quattro",
            "Cambio: S tronic de 7 velocidades",
            "0-100 km/h: 3,1 segundos",
            "Velocidade maxima: 331 km/h"
        ]
    ),
    Carro(
        id=2,
        nome="Bugatti Chiron Sport",
        preco=50000000.00,
        imagem="assets/carro3.jfif",
        descricao=(
            "O Bugatti Chiron Sport e um hiperesportivo "
            "com motor W16 de 8.0 litros e quatro "
            "turbocompressores."
        ),
        especificacoes=[
            "Motor: W16 8.0 quadriturbo",
            "Potencia: 1.500 cv",
            "Torque: 1.600 Nm",
            "Tracao: integral",
            "Cambio: dupla embreagem de 7 velocidades",
            "0-100 km/h: 2,4 segundos",
            "Velocidade maxima: 420 km/h"
        ]
    )
]


def listar_carros():
    return carros


def buscar_carro(id_carro: int):
    for carro in carros:
        if carro.id == id_carro:
            return carro

    return None


def adicionar_carro(dados: CarroCriacao):
    novo_id = max((carro.id for carro in carros), default=0) + 1

    novo_carro = Carro(
        id=novo_id,
        **dados.model_dump()
    )

    carros.append(novo_carro)

    return novo_carro


def atualizar_carro(id_carro: int, dados: CarroCriacao):
    carro = buscar_carro(id_carro)

    if carro is None:
        return None

    atualizado = Carro(
        id=id_carro,
        **dados.model_dump()
    )

    indice = carros.index(carro)
    carros[indice] = atualizado

    return atualizado


def excluir_carro(id_carro: int):
    carro = buscar_carro(id_carro)

    if carro is None:
        return False

    carros.remove(carro)

    return True
