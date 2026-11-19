from app.database.conexao import conectar


def popular_carros():

    carros_iniciais = [
        (
            "Audi R8 V10 Performance",
            1310990.00,
            "assets/carro2.jpg",
            (
                "O Audi R8 V10 Performance quattro possui "
                "motor V10 5.2 FSI aspirado, alto desempenho "
                "e tracao integral quattro."
            ),
            [
                "Motor: V10 5.2 FSI",
                "Potencia: 620 cv",
                "Torque: 580 Nm",
                "Tracao: quattro",
                "Cambio: S tronic de 7 velocidades",
                "0-100 km/h: 3,1 segundos",
                "Velocidade maxima: 331 km/h"
            ]
        ),
        (
            "Bugatti Chiron Sport",
            50000000.00,
            "assets/carro3.jfif",
            (
                "O Bugatti Chiron Sport e um hiperesportivo "
                "com motor W16 de 8.0 litros e quatro "
                "turbocompressores."
            ),
            [
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

    conexao = conectar()

    try:
        with conexao.cursor() as cursor:

            cursor.execute(
                "SELECT COUNT(*) FROM carros;"
            )

            quantidade = cursor.fetchone()[0]

            if quantidade == 0:

                for carro in carros_iniciais:

                    cursor.execute("""
                                   INSERT INTO carros (
                                       nome,
                                       preco,
                                       imagem,
                                       descricao,
                                       especificacoes
                                   )
                                   VALUES (%s, %s, %s, %s, %s);
                                   """, carro)

                print("Carros iniciais cadastrados com sucesso!")

            else:
                print("O banco ja possui carros. Nenhuma insercao realizada.")

        conexao.commit()

    except Exception:
        conexao.rollback()
        raise

    finally:
        conexao.close()