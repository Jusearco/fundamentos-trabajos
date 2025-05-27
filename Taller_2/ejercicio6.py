def evaluar_polinomio(coefs, x):
    return sum(c * x ** i for i, c in enumerate(reversed(coefs)))

def calcular_area(coefs, n):
    ancho = 1 / n
    area = 0
    for i in range(n):
        x = i * ancho
        y = evaluar_polinomio(coefs, x)
        if y < 0:
            y = 0
        elif y > 1:
            y = 1
        area += y * ancho
    return area

def procesar_entrada():
    while True:
        grado = int(input())
        if grado == 20:
            break
        coefs = list(map(int, input().split()))
        n = int(input())

        area_cain = calcular_area(coefs, n)
        area_abel = 1 - area_cain

        if abs(area_cain - area_abel) <= 0.001:
            print("JUSTO")
        elif area_cain > area_abel:
            print("CAIN")
        else:
            print("ABEL")

if __name__ == "__main__":
    procesar_entrada()
