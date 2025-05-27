def encontrar_pares(lista, objetivo):
    vistos = set()
    pares = set()
    for num in lista:
        complementario = objetivo - num
        if complementario in vistos:
            pares.add(tuple(sorted((num, complementario))))
        vistos.add(num)
    for par in pares:
        print(f"{par[0]}, {par[1]}")

lista = [1, 2, 3, 4, 3, 5, 6]
objetivo = 7
encontrar_pares(lista, objetivo)
