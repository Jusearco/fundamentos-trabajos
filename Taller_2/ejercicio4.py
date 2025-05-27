import math

def menor_factor_para_cuadrado_perfecto(n):
    factores = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factores[i] = factores.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factores[n] = factores.get(n, 0) + 1

    resultado = 1
    for factor, cantidad in factores.items():
        if cantidad % 2 != 0:
            resultado *= factor
    return resultado

casos = [8, 10, 30]
for c in casos:
    print(menor_factor_para_cuadrado_perfecto(c))
