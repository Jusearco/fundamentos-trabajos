def a_romano(n):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    resultado = ""
    for val, rom in valores:
        while n >= val:
            resultado += rom
            n -= val
    return resultado

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    print(a_romano(numero))
