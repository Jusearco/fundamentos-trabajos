import string

def cifrar_cesar(texto):
    def cifrar_palabra(palabra, salto):
        alfabeto = string.ascii_lowercase
        resultado = ""
        for c in palabra:
            if c.lower() in alfabeto:
                indice = alfabeto.index(c.lower())
                nuevo_indice = (indice + salto) % 26
                nueva_letra = alfabeto[nuevo_indice]
                resultado += nueva_letra.upper() if c.isupper() else nueva_letra
            else:
                resultado += c
        return resultado

    palabras = texto.split()
    resultado = []
    for i, palabra in enumerate(palabras):
        salto = 4 if i % 2 == 0 else 3
        resultado.append(cifrar_palabra(palabra, salto))
    return " ".join(resultado)

def descifrar_cesar(texto):
    def descifrar_palabra(palabra, salto):
        alfabeto = string.ascii_lowercase
        resultado = ""
        for c in palabra:
            if c.lower() in alfabeto:
                indice = alfabeto.index(c.lower())
                nuevo_indice = (indice - salto) % 26
                nueva_letra = alfabeto[nuevo_indice]
                resultado += nueva_letra.upper() if c.isupper() else nueva_letra
            else:
                resultado += c
        return resultado

    palabras = texto.split()
    resultado = []
    for i, palabra in enumerate(palabras):
        salto = 4 if i % 2 == 0 else 3
        resultado.append(descifrar_palabra(palabra, salto))
    return " ".join(resultado)
