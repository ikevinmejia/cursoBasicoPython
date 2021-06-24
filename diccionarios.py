def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
        "llave4": 4,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina": 44938712,
        "Brazil": 210147125,
        "Colombia": 503722424,
    }
    # print(poblacion_paises["Argentina"])

    # for i in poblacion_paises.keys():
    #     print(i)

    for i in poblacion_paises.values():
        print(i)

    """ for i, j in poblacion_paises.items():
         print(i + " tiene " + str(j) + " habitantes") """

if __name__ == "__main__":
    run()