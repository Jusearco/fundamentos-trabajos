import itertools

def permutaciones_unicas(cadena):
    caracteres = sorted(set(cadena))
    permuts = itertools.permutations(caracteres)
    return [''.join(p) for p in permuts]

cadena = "abcfga"
resultados = permutaciones_unicas(cadena)
for r in resultados:
    print(r)
