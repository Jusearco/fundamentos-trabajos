def factorial (n):
    fac_numero = 1
    for i in range(1,n+1):
        fac_numero = fac_numero*i
    return(fac_numero)



numero = int(input("inserte un numero: "))

w = factorial(numero) 



print("el resultado es", w)
print(w)